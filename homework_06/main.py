"""
Домашнее задание "Взаимодействие между контейнерами"
Задача:
- создайте docker-compose файл, настройте там связь базы данных и веб-приложения
- добавьте в свой проект модели. Это могут быть те же модели, что были использованы для сохранения данных с открытого API, это может быть и что-то новое
- добавьте возможность создавать новые записи
- создайте страницу, на которой эти записи выводятся
- база данных должна быть в отдельном контейнере
- Flask приложение должно запускаться не в debug режиме, а в production-ready (uwsgi, nginx, gunicorn)

"""
from os import getenv
from flask import Flask, render_template, request, url_for, redirect
from flask_migrate import Migrate

from forms.product_create import CreateProductForm
from models import db, Product

app = Flask(__name__)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="index_page")
def index():
    return render_template("index.html")


@app.route("/about/", endpoint="about_page")
def about():
    return render_template("about.html")


@app.route("/products/", endpoint="products_list")
def get_products():
    products = Product.query.order_by(Product.id).all()
    return render_template("products/list.html", products=products)


@app.route("/products/add", methods=["GET", "POST"], endpoint="products_add")
def add_product():
    form = CreateProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data
    product = Product(name=product_name)
    db.session.add(product)
    db.session.commit()

    url = url_for("products_list")
    return redirect(url)


if __name__ == '__main__':
    app.run(debug=True)
