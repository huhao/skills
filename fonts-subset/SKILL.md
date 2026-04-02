---
name: fonts-subset
description: 使用 pyftsubset 精简字体，支持 WOFF2 格式，常用于 web 字体优化场景。
---

# fonts-subset

该 Skill 旨在利用 `fonttools` 提供的 `pyftsubset` 命令，对字体（TTF/OTF）进行精简（Subsetting），仅保留需要的字符集（Glyphs），从而大幅度减小字体文件体积。

## 1. 环境准备 (Installation)

你需要安装 `fonttools` 以及用于 WOFF2 压缩的 `brotli`。

```bash
pip install fonttools brotli
```

## 2. 基础用法 (Basic Usage)

### 根据字符列表精简 (By Text)
提供需要保留的字符，输出 WOFF2。

```bash
pyftsubset "your-font.ttf" --text="床前明月光疑是地上霜" --flavor=woff2 --output-file="font-subset.woff2"
```

### 根据 Unicode 范围精简 (By Unicode)
保留指定的 Unicode 范围。

```bash
# 保留基本键盘字符 (ASCII)
pyftsubset "your-font.ttf" --unicodes="U+0000-007F" --flavor=woff2 --output-file="font-basic.woff2"
```

### 根据字符集文件精简 (By Text File)
如果你有一个包含所有需要字符的文本文件（例如 `chars.txt`）：

```bash
pyftsubset "your-font.ttf" --text-file="chars.txt" --flavor=woff2 --output-file="font-subset.woff2"
```

## 3. 进阶参数说明 (Advanced Parameters)

- `--flavor=woff2`: 指定输出格式。常用 woff2，因为它具有极高的压缩比。
- `--layout-features='*'` (默认): 保留 OpenType 特性（如 Kerning, Ligatures）。如果追求极致体积，可以使用 `*` 以外的具体特性或留空。
- `--no-subset-tables+=...`: 指定不进行子集化的表格。
- `--notdef-outline`: 保留缺失字符的轮廓（通常建议保留）。

## 4. 常见场景 (Common Scenarios)

### 场景 A：精简网页特定的文字
常用于网页标题或特定的标语（Slogan）。

### 场景 B：保留常用字符集
该 Skill 附带了一个最小字符集模板 `resources/minimal_chars.txt`，包含常见标点和极高频汉字。

```bash
# 使用本 Skill 目录下的脚本
python3 scripts/subset.py "SourceHanSans.otf" --text-file "resources/minimal_chars.txt"
```

## 5. 本 Skill 提供的工具集 (Included Tools)

- **`scripts/subset.py`**: 一个 Python 封装脚本，带有基础的依赖检查逻辑，自动输出 woff2 格式。
- **`resources/minimal_chars.txt`**: 包含 ASCII 和极高频的中文字符及标点。

## 6. 建议 & 提示 (Tips)

1. **备份原始字体**: 精简是不可逆的，始终保留一份完整的 TTF/OTF 原文件。
2. **字符排查**: 如果发现精简后的字体在某些设备上显示异常（出现豆腐块），请检查是否漏掉了空格 ` `、标点符号或特定的变体字符。
3. **性能**: `woff2` 是目前 Web 端事实上的标准，强烈建议使用 `--flavor=woff2`。
