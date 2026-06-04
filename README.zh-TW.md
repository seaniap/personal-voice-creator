# Personal Voice Creator（個人風格 Skill 產生器）

> 一個可安裝的 Claude skill，幫你打造**屬於你自己**的寫作風格 skill——讓 Claude 寫出來的文章、書信、貼文，真的像你寫的。

**語言：** [English](README.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

---

## 它能做什麼

AI 寫的東西總是有股「通用感」。**Personal Voice Creator** 透過一段輕鬆的對話流程，把你的風格固化成一個可重複使用的 skill：

1. **訪談** — Claude 問你幾個關於寫作習慣的問題
2. **樣本** — 你提供幾篇寫過的東西（連結、貼上文字，或上傳檔案）
3. **測試與校準** — Claude 寫測試稿，你修改到它聽起來像你為止
4. **打包** — 你得到一個可以永久安裝使用的 `personal-voice.skill`

關鍵在第三步。每一句「不對，我會這樣說」的修正都會被記下來——因為你真正的聲音，就藏在「你以為你怎麼寫」和「你實際怎麼寫」的那道縫裡。

## 快速開始

### 1. 安裝產生器 skill

下載 [`dist/personal-voice-creator.skill`](dist/personal-voice-creator.skill)，在 Claude 進入 **設定 → Skills**，上傳這個檔案。

### 2. 啟動它

開一個新對話，跟 Claude 說：

> 幫我建立我的個人風格 skill。

Claude 會開始訪談你、請你提供寫作樣本、寫測試稿，並根據你的回饋校準。

### 3. 拿到你的專屬 skill

流程結束時，Claude 會產出一個為你量身打造的 `personal-voice.skill`。用同樣方式安裝（**設定 → Skills**），之後隨時可以這樣觸發：

> 用我的風格寫這篇。

## 你需要準備

- 一個已啟用 Skills 的 Claude 帳號
- 幾篇真實的寫作樣本（越真實越好）
- 15～20 分鐘進行訪談與校準

## 專案結構

```
.
├── README.md / README.zh-TW.md / README.ja.md   說明文件（英文為正式版本）
├── BUILD_LOG.md           這個專案怎麼做出來的（故事＋心得）
├── DESIGN.md              一頁的設計理念
├── CLAUDE.md              給 Claude Code 的專案記憶
├── skill/
│   └── personal-voice-creator/    skill 原始檔（在這裡修改）
├── dist/
│   └── personal-voice-creator.skill   打包好的檔案（下載這個）
└── examples/              範例流程
```

## 從原始碼重新打包

如果你修改了 skill，重新打包 `.skill` 檔案：

```bash
pip install pyyaml
python skill/personal-voice-creator/scripts/package_skill.py skill/personal-voice-creator dist
```

打包前會自動驗證結構，結構壞掉就不會產出檔案。

## 參與貢獻

歡迎開 Issue 或送 Pull Request。每個 PR 都會自動檢查 skill 是否還能正常打包。專案慣例請見 `CLAUDE.md`。

## 授權

MIT — 詳見 [LICENSE](LICENSE)。
