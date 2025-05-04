#!/usr/bin/env python
# データベースにデータを追加するスクリプト

from models.database import db_session
from models.models import OnegaiContent

# データの作成
c1 = OnegaiContent("お願いします", "5000兆円ください")
c2 = OnegaiContent("助けてください", "ぽんぽんぺいん")
c3 = OnegaiContent("許してください", "なんでもしますから")

# データベースへの追加
db_session.add(c1)
db_session.add(c2)
db_session.add(c3)
db_session.commit()

print("3件のデータをデータベースに追加しました")