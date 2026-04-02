---
name: deploy-android-device
description: 自动化编译 Android 应用并部署到物理设备
---

# Deploy Android Device Skill

此技能用于在 Android 开发中快速完成「编译 -> 安装 -> 运行」的全流程。

## 部署流程

1. **环境自检 (ADB Check)**
   - 执行 `adb devices` 确认设备已连接且状态为 `device`。

2. **脚本探测 (Deployment Strategy)**
   - 检查项目根目录下是否存在： `scripts/deploy.sh`。
   - **优先使用项目特定脚本**：
     - 如果脚本存在，赋予执行权限并执行： `chmod +x scripts/deploy.sh && ./scripts/deploy.sh`。
   - **后备标准模式 (Gradle Fallback)**：
     - 如果脚本不存在，执行： `./gradlew installDebug`。

## 核心指令
[ -f scripts/deploy.sh ] && chmod +x scripts/deploy.sh && ./scripts/deploy.sh || ./gradlew installDebug
