from autoflyer import db
from datetime import datetime


class items(db.Model):  # type: ignore
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True) # システムで使う番号
    name = db.Column(db.String(80),nullable=False) #商品名
    price = db.Column(db.INT(),nullable=False) #価格
    img = db.Column(db.String(),nullable=True) #画像(未整備)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now) #作成日時
    bio = db.Column(db.String(100),nullable=True) #説明
    storename = db.Column(db.String(80),nullable=True) #店の名前
    importance = db.Column(db.INT(),nullable=True,default=1) #重要度