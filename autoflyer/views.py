from flask import render_template ,request,jsonify
from autoflyer import app
from autoflyer.models.items import items
from autoflyer import db

@app.route('/')
def index():
    return render_template('autoflyer/index.html')
@app.route('/api/',methods=["GET"])
def apiget():
    storenameget = request.args.get("storename")
    qu = db.session.query(items).filter_by(storename="仮ストア").all()
    a=0 #quのレコード数
    for name in qu:
        a= a + 1
    print(a)
    c = []
    #{‘key1’: 10, ‘key2’: 20, ‘key3’: 30}
    for num in range(a):
       c.append({"name":qu[num].name,"price":qu[num].price,"bio":qu[num].bio,"importance":qu[num].importance,"created_at":qu[num].created_at})
    print(c)
    return jsonify(c)

    
@app.route('/test',methods=["GET"])
def test():
    adddata = items(
    name="人参",
    price = 50,
    bio = "おいしい人参です。",
    storename="仮ストア"
    )
    db.session.add(adddata)
    db.session.commit()
