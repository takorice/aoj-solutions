# aoj-solutions

## 概要
Goでaojの問題を解くための環境
コマンド一つで以下を自動的に行う
- テンプレートから実行ファイル、テストファイルを作成する
- aojからテストケースを取得する

## 利用するツール
- contest.go
  - https://github.com/yaegashi/contest.go
- aoj cli
  - https://github.com/travelist/aoj-cli
- Python3製の自家製ツール
  - util/new-solution.py

## 開始方法
### 初回セットアップ
```bash
# aoj cli install (for Mac)
$ brew tap travelist/homebrew-aoj-cli
$ brew install aoj

# aoj cli init
$ aoj init

# contest.go install
$ go get github.com/yaegashi/contest.go/cmd/contest-cli
```

### 解答用のディレクトリ、テンプレート、テストケースを作成
```bash
# change directory
$ cd courses
# run tool
$ python ../util/new-solution.py [PROBLEM-ID]
```