from flask import Flask,request
import json
from eventTest import test_result
app=Flask(__name__)

#只接受get访问
@app.route("/test",methods=["GET"])
def check():
    return_dict={'return_code':'200','return_info':'查询成功','result':False}
    get_data=request.args.to_dict()
    oid=get_data.get('oid')
    return_dict['result']=test_result(oid)
    return json.dumps(return_dict,ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
