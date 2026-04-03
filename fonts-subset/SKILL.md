---
name: fonts-subset
description: 使用 pyftsubset 精简字体
---

# fonts-subset

该 Skill 旨在利用 `fonttools` 提供的 `pyftsubset` 命令，对字体（TTF/OTF）进行精简（Subsetting），仅保留需要的字符集（Glyphs），从而大幅度减小字体文件体积。

## 1. 环境准备 (Installation)

你需要安装 `fonttools` 以及用于 WOFF2 压缩的 `brotli`。

```bash
pip install fonttools brotli
```

## 2. 基础用法 (Basic Usage)

### 根据字符集文件精简 (By Text File)

指定了文件，优先取指定的文件，没有指定，则默认使用resources/chars.txt文件
字体格式跟源文件保持一致，输出文件名是源文件名-subset
输出路径：源文件所在目录

```bash
pyftsubset your-font.otf --text-file=chars.txt --output-file=your-font-subset.otf
```