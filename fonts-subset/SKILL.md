---
name: fonts-subset
description: 使用 pyftsubset 精简字体
---

# fonts-subset
该 Skill 旨在利用 `fonttools` 提供的 `pyftsubset` 命令，对字体进行精简（Subsetting），仅保留需要的字符集（Glyphs），从而大幅度减小字体文件体积。


## ℹ️ 字体源文件

| 字体 | 文件 |
| --- | --- |
| 思源宋体 | `resources/fonts/SourceHanSerifSC-Regular.otf` |
| 花园明朝体 | `resources/fonts/HanaMinA.ttf` |

## ℹ️ 字符集

resources/chars.txt

## ℹ️ 字体输出格式及目录
字体格式跟源文件保持一致，输出文件名是源文件名-subset，输出目录 resources/fonts/output


```bash
pyftsubset your-font.otf --text-file=chars.txt --output-file=your-font-subset.otf
```

