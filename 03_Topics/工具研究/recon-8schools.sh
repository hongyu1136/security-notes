#!/bin/bash
# 贵州 8 校子域名侦察 — 全自动流水线
# 用法: chmod +x recon-8schools.sh && ./recon-8schools.sh
# 产出: ./recon-output/{学校}/ 子域列表 + 存活检测 + nuclei 扫描

set -e
TIMESTAMP=$(date +%Y%m%d_%H%M)
OUTDIR="./recon-output"
mkdir -p "$OUTDIR"

# ====== 目标列表 ======
declare -A SCHOOLS
SCHOOLS[gzu]="gzu.edu.cn"
SCHOOLS[gznu]="gznu.edu.cn"
SCHOOLS[gmc]="gmc.edu.cn"
SCHOOLS[git]="git.edu.cn"
SCHOOLS[gzmu]="gzmu.edu.cn"
SCHOOLS[gznc]="gznc.edu.cn"
SCHOOLS[lpssy]="lpssy.edu.cn"
SCHOOLS[kluniv]="kluniv.edu.cn"

echo "=========================================="
echo " 贵州 8 校侦察 — $TIMESTAMP"
echo "=========================================="

for CODE in "${!SCHOOLS[@]}"; do
    DOMAIN="${SCHOOLS[$CODE]}"
    echo ""
    echo "===== [$CODE] $DOMAIN ====="
    WORKDIR="$OUTDIR/$CODE"
    mkdir -p "$WORKDIR"

    # Step 1: crt.sh 被动收集
    echo "[1/4] crt.sh passive ..."
    curl -s --max-time 30 "https://crt.sh/?q=%25.$DOMAIN&output=json" | \
        jq -r '.[].name_value' 2>/dev/null | \
        tr ',' '\n' | sed 's/^\*\.//' | sed 's/^www\.//' | \
        sort -u > "$WORKDIR/crtsh_raw.txt" || true

    # Step 2: subfinder 主动发现
    echo "[2/4] subfinder active ..."
    subfinder -d "$DOMAIN" -silent -timeout 10 2>/dev/null | \
        sed 's/^\*\.//' | sort -u > "$WORKDIR/subfinder.txt" || true

    # Step 3: 合并去重
    cat "$WORKDIR/crtsh_raw.txt" "$WORKDIR/subfinder.txt" 2>/dev/null | \
        sort -u > "$WORKDIR/all_subs.txt"
    SUB_COUNT=$(wc -l < "$WORKDIR/all_subs.txt")
    echo "       => $SUB_COUNT unique subdomains"

    # Step 4: httpx 存活检测 + 指纹
    echo "[3/4] httpx live check ..."
    cat "$WORKDIR/all_subs.txt" | \
        httpx -silent -timeout 8 -title -status-code -tech-detect -fc 404,400 \
        -o "$WORKDIR/live_hosts.txt" 2>/dev/null || true
    LIVE_COUNT=$(wc -l < "$WORKDIR/live_hosts.txt" 2>/dev/null || echo 0)
    echo "       => $LIVE_COUNT live hosts"

    # Step 5: nuclei 漏洞扫描 (仅扫描存活的)
    echo "[4/4] nuclei scan ..."
    if [ -s "$WORKDIR/live_hosts.txt" ]; then
        nuclei -l "$WORKDIR/live_hosts.txt" \
            -t ~/nuclei-templates/http/ \
            -severity critical,high,medium \
            -timeout 10 -silent \
            -o "$WORKDIR/nuclei_results.txt" 2>/dev/null || true
        VULN_COUNT=$(wc -l < "$WORKDIR/nuclei_results.txt" 2>/dev/null || echo 0)
        echo "       => $VULN_COUNT findings"
    else
        echo "       跳过 — 无存活主机"
    fi
done

echo ""
echo "=========================================="
echo " 侦察完成 — 结果: $OUTDIR/"
echo "=========================================="
for CODE in "${!SCHOOLS[@]}"; do
    WORKDIR="$OUTDIR/$CODE"
    LIVE=$(wc -l < "$WORKDIR/live_hosts.txt" 2>/dev/null || echo 0)
    VULN=$(wc -l < "$WORKDIR/nuclei_results.txt" 2>/dev/null || echo 0)
    echo "  $CODE (${SCHOOLS[$CODE]}): $LIVE live | $VULN findings"
done
echo ""
echo "下一步: grep -r 'critical\|high' recon-output/*/nuclei_results.txt"
