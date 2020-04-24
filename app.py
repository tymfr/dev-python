from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    nums = [1, 2, 3, 4]
    province = ["大同北", "大同南", "朔州", "吕梁北", "吕梁南", "太原", "晋中", "太旧", "长治"]
    title = "山西省交通大数据分析平台"
    cars = ["小型车", "中型车", "大型车"]
    context = {"transports": [
        {"transporttype": "公路运输", "passengervolume": random.randint(2000, 10000),
         "traffic": random.randint(1000, 6000)},
        {"transporttype": "公路运输", "passengervolume": random.randint(2000, 10000),
         "traffic": random.randint(1000, 8000)},
        {"transporttype": "公路运输", "passengervolume": random.randint(2000, 10000),
         "traffic": random.randint(1000, 7000)},
    ]}

    return render_template("index.html", province=province, title=title, **context, cars=cars, nums=nums)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
