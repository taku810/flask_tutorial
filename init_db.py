#!/usr/bin/env python
# データベース初期化用スクリプト

from models.database import init_db

print("データベースを初期化します...")
init_db()
print("データベースの初期化が完了しました")