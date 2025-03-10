# 百词斩离线词库提取 / Baicizhan Offline Dictionary Extraction

## 项目概述 / Project Overview
- 本仓库收录了百词斩热门词库的解析数据，提供结构化存储的SQLite数据库和快速查询工具。所有词库数据均通过解析ZPK文件获得，按教材分类整理，便于开发者进行二次开发。

- This repository contains parsed data from popular Baicizhan vocabulary libraries, providing a structured SQLite database and fast query tools. All vocabulary data is obtained by parsing ZPK files, organized by textbook categories for developers' secondary development.

## 技术细节 / Technical Details
### 数据来源 / Data Source
- 基于开源项目 [parseZpk](https://github.com/KarasuShin/parseZpk) 解析 / Based on open-source project [parseZpk](https://github.com/KarasuShin/parseZpk)
- 包含大部分的百词斩官方词库 / Contains most of the official thesaurus
- 文件已按教材分类存储 / Files organized by textbook categories

### 词库内容 / Content
- 📚 basic4000词汇
- 📚 GMAT词汇
- 📚 GRE词汇
- 📚 MAT词汇
- 📚 PETS词汇
- 📚 PET词汇
- 📚 高考词汇
- 📚 考研词汇
- 📚 六级词汇
- 📚 四级词汇
- 📚 托福词汇
- 📚 新概念词汇
- 📚 雅思词汇
- 📚 中考词汇
- 📚 专八词汇
- 📚 专升本词汇
- 📚 专四词汇


**⚠️警告：由于数据量巨大，暂时未完全上传完成，将于后续陆续上传。**


**⚠️Warning: Due to the huge amount of data, the complete upload has not been completed for the time being, and will be uploaded one after another.**

### 数据库结构 / Database Schema
- 数据库文件 / Database file：`word.db`  
- 表结构说明 / Table structure：

| 字段名 / Column| 类型 / Type   | 说明 / Description          |
|---------------|---------|----------------|
| word          | 字符串 / str    | 单词原文 / Original word     |
| mean_cn       | 字符串 / str    | 中文释义 / Chinese definition     |

## 使用工具 / Tools
- 提供Python查询工具：`find.py`，默认输入英文可查询中文
- Provide Python query tool: `find.py`, default input English can query Chinese

## 免责声明 / Disclaimer
- 本仓库所有数据仅供学习交流使用，不得用于商业用途。数据版权归百词斩所有，请于下载后24小时内删除。
- All data in this repository is for educational purposes only. Commercial use is prohibited. Copyright belongs to Baicizhan. Please delete within 24 hours after downloading.

## 联系作者 / Contact
- 📬 电子邮箱 / Email: zhang.ershi@qq.com
- 💬 微信号 / WeChat: zhang_tjnk
