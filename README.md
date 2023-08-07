# zxext
*智学网的补充库*

![](https://img.shields.io/badge/License-ASOUL-red) ![](https://img.shields.io/badge/Python-3.8+-green) ![](https://img.shields.io/pypi/v/zxext)

收录了一些智学网库里比较冷门的函数。

**一个版本仅对应一个智学网的版本！**



### 对应关系

| zhixue-ext版本 | 对应zhixuewang版本 |
| :------------: | :----------------: |
|  0.1.0-0.1.1   |       1.1.11       |



## 支持的功能

1. 练习本功能（`workbook`）



## 问题和建议

如果您在使用的过程中遇到任何问题，欢迎前往 [Issue](https://github.com/anwenhu/zhixuewang/issues)提问
当然也可以加入这个QQ群讨论：862767072（备注：智学网扩展）



### 示例

```python
from zxext.workbook import Workbook # 导入练习本
from zhixuewang import * # 导入核心库

teacher = login("114514", "1919810")
wb = Workbook(teacher.get_session())
print(wb.search_press("人教"))
# >> 272
```

