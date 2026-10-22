# Tech Service (تک سرویس)

وب‌سایت شرکتی و ارائه خدمات فنی و مهندسی مبتنی بر جنگو (Django).

---

## 🚀 ویژگی‌ها و ماژول‌ها
- **صفحه اصلی (Home):** معرفی خدمات، بنرها و مزایا
- **خدمات (Services):** معرفی دسته‌بندی و جزئیات خدمات فنی
- **نمونه‌کارها (Portfolio):** نمایش پروژه‌های انجام‌شده همراه با فیلتر دسته‌بندی
- **وبلاگ (Blog):** مقالات و اخبار تکنولوژی
- **درباره ما (About):** معرفی تیم و اهداف شرکت
- **تماس با ما (Contact):** فرم تماس و راه‌های ارتباطی
- **محاسبه قیمت (Pricing):** ابزار هوشمند محاسبه تخمینی هزینه‌ها
- **درخواست پیش‌فاکتور (Quote):** فرم ثبت درخواست سفارش و استعلام قیمت
- **سئو و بهینه‌سازی (SEO):** ساخت خودکار سایت‌مپ و تگ‌های متای استاندارد

---

## 🛠 نیازمندی‌ها و فناوری‌ها
- Python 3.10+
- Django 5.x
- Bootstrap & Vazirmatn Font
- SQLite (توسعه) / PostgreSQL (محیط عملیاتی)

---

## ⚙️ راه‌اندازی در محیط محلی (Local Development)

۱. **کلون کردن مخزن:**
```bash
git clone https://github.com/shahabshahrokkh/tech-service.git
cd tech-service
```

۲. **ساخت و فعال‌سازی محیط مجازی (Virtual Environment):**
```bash
python -m venv venv
# در ویندوز:
venv\Scripts\activate
# در لینوکس/مک:
source venv/bin/activate
```

۳. **نصب وابستگی‌ها:**
```bash
pip install -r requirements.txt
```

۴. **تنظیم متغیرهای محیطی:**
فایل `.env.example` را کپی کرده و به نام `.env` ذخیره کنید:
```bash
cp .env.example .env
```

۵. **اجرای مایگریشن‌ها:**
```bash
python manage.py migrate
```

۶. **اجرای سرور توسعه:**
```bash
python manage.py runserver
```
سپس مرورگر خود را در آدرس `http://127.0.0.1:8000` باز کنید.

---

## 🌐 استقرار (Deployment)
این پروژه دارای کانفیگ‌های آماده برای استقرار روی:
- **PythonAnywhere** (فایل کانفیگ WSGI: `pythonanywhere_wsgi.py`)
- **Liara** (فایل کانفیگ: `liara.json`)
می‌باشد.
