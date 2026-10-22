"""
Management command to seed realistic Persian demonstration data.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.core.models import SiteSettings, Slider, Testimonial, WorkProcess
from apps.services.models import Service, ServiceFeature
from apps.portfolio.models import Project, ProjectCategory
from apps.pricing.models import PricingCategory, PricingModule, PricingPreset
from apps.blog.models import Article, ArticleCategory
from apps.about.models import TeamMember, CompanyStat


class Command(BaseCommand):
    help = 'Seeds initial demonstration data matching bamboweb agency structure'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))

        # 1. Site Settings
        settings = SiteSettings.load()
        settings.site_name = 'تک سرویس'
        settings.tagline = 'طراحی و توسعه تخصصی وب‌سایت، CRM و نرم‌افزار'
        settings.description = 'ما وب‌سایت‌ها و سیستم‌های نرم‌افزاری اختصاصی با استانداردهای روز دنیا، سرعت بسیار بالا و سئوی فنی قدرتمند طراحی می‌کنیم.'
        settings.phone_1 = '۰۲۱-۸۸۸۸۹۹۹۹'
        settings.phone_2 = '۰۹۱۲۳۴۵۶۷۸۹'
        settings.email = 'info@techservice.ir'
        settings.address = 'تهران، خیابان ولیعصر، بالاتر از میدان ونک، برج فناوری، طبقه ۸'
        settings.working_hours = 'شنبه تا چهارشنبه ۹:۰۰ الی ۱۸:۰۰ | پنج‌شنبه ۹:۰۰ الی ۱۳:۰۰'
        settings.instagram = 'https://instagram.com'
        settings.telegram = 'https://t.me'
        settings.whatsapp = '989123456789'
        settings.linkedin = 'https://linkedin.com'
        settings.github = 'https://github.com'
        settings.save()
        self.stdout.write('[OK] Site settings seeded.')

        # 2. Work Process
        WorkProcess.objects.all().delete()
        WorkProcess.objects.create(
            title='تحلیل و نیازسنجی دقیق',
            description='بررسی دقیق اهداف بیزینس، تحلیل رقبای بازار و تهیه سند مشخصات فنی (PRD).',
            order=1
        )
        WorkProcess.objects.create(
            title='طراحی رابط کاربری (UI/UX)',
            description='طراحی وایرفریم‌ها و پروتوتایپ در فیگما با رعایت اصول روانشناسی رنگ و تجربه کاربری.',
            order=2
        )
        WorkProcess.objects.create(
            title='توسعه و کدنویسی استاندارد',
            description='پیاده‌سازی بک‌اند قدرتمند با Django و فرانت‌اند مدرن، پرسرعت و واکنش‌گرا.',
            order=3
        )
        WorkProcess.objects.create(
            title='تست، تحویل و پشتیبانی',
            description='تست‌های امنیت، بهینه‌سازی سرعت و سئو، راه‌اندازی هاست و ارائه ۶ ماه پشتیبانی رایگان.',
            order=4
        )
        self.stdout.write('[OK] Work process seeded.')

        # 3. Services & Features
        Service.objects.all().delete()
        s1 = Service.objects.create(
            title='طراحی و توسعه وب‌سایت اختصاصی',
            slug='web-development',
            short_description='طراحی سایت‌های شرکتی، فروشگاهی و خدماتی با کدنویسی اختصاصی، امنیت بالا و سرعت فوق‌العاده.',
            description='ما وب‌سایت شما را بر اساس نیاز دقیق کسب‌وکارتان کدنویسی می‌کنیم. استفاده از فریمورک قدرتمند جنگو و استانداردهای روز فرانت‌اند، سرعتی باورنکردنی و انعطاف‌پذیری بی‌نهایت را برای توسعه آینده به ارمغان می‌آورد.',
            order=1
        )
        ServiceFeature.objects.create(service=s1, title='طراحی ۱۰۰٪ واکنش‌گرا و ریسپانسیو', order=1)
        ServiceFeature.objects.create(service=s1, title='سرعت بارگذاری زیر ۱ ثانیه (PageSpeed 95+)', order=2)
        ServiceFeature.objects.create(service=s1, title='سئوی فنی و ساختار استاندارد Schema', order=3)
        ServiceFeature.objects.create(service=s1, title='پنل مدیریت محتوای روان و کاملاً فارسی', order=4)

        s2 = Service.objects.create(
            title='توسعه سیستم‌های مدیریت مشتریان (CRM)',
            slug='crm-development',
            short_description='سامانه‌های اختصاصی اتوماسیون فروش، مدیریت پرونده مشتریان و گزارش‌گیری تحلیلی.',
            description='یک CRM اختصاصی به شما امکان می‌دهد فرآیندهای فروش، پیگیری سرنخ‌ها، ثبت قراردادها و ارتباطات تلفنی و پیامکی را به طور یکپارچه کنترل کنید.',
            order=2
        )
        ServiceFeature.objects.create(service=s2, title='مدیریت هوشمند سرنخ‌ها و لیدهای ورودی', order=1)
        ServiceFeature.objects.create(service=s2, title='داشبورد تحلیلی و نمودارهای مالی و فروش', order=2)
        ServiceFeature.objects.create(service=s2, title='اتصال به وب‌سرویس پیامک و سانترال ویپ', order=3)

        s3 = Service.objects.create(
            title='سیستم مدیریت محتوا و پلتفرم‌های ابری (CMS)',
            slug='cms-development',
            short_description='پنل‌های محتوایی اختصاصی بدون باگ، بسیار سبک و بدون نیاز به پلاگین‌های آسیب‌پذیر.',
            description='جایگزین امن و فوق‌العاده سریع برای سیستم‌های سنتی؛ سیستم CMS اختصاصی ما بدون سربار کدهای سنگین و آسیب‌پذیری‌های امنیتی به شما کنترل کامل محتوا را می‌دهد.',
            order=3
        )
        ServiceFeature.objects.create(service=s3, title='مدیریت چندسطحی دسترسی ادمین‌ها', order=1)
        ServiceFeature.objects.create(service=s3, title='بهینه‌سازی خودکار تصاویر به فرمت مدرن WebP', order=2)
        ServiceFeature.objects.create(service=s3, title='سیستم وبلاگ‌نویسی و تولید لندینگ‌پیج سریع', order=3)
        self.stdout.write('[OK] Services seeded.')

        # 4. Portfolio Categories & Projects
        ProjectCategory.objects.all().delete()
        c_corp = ProjectCategory.objects.create(name='شرکتی و صنعتی', slug='corporate', order=1)
        c_shop = ProjectCategory.objects.create(name='فروشگاهی', slug='ecommerce', order=2)
        c_serv = ProjectCategory.objects.create(name='خدماتی و پلتفرمی', slug='services', order=3)
        c_port = ProjectCategory.objects.create(name='شخصی و نمونه‌کار', slug='personal', order=4)

        Project.objects.all().delete()
        Project.objects.create(
            title='پلتفرم سرمایه‌گذاری آریا فین‌تک',
            slug='aria-fintech',
            category=c_corp,
            short_description='طراحی پورتال شرکتی و سامانه گزارش‌دهی آنلاین دارایی‌ها برای هلدینگ سرمایه‌گذاری آریا.',
            description='در این پروژه علاوه بر طراحی مدرن دارک‌مود، اتصال به APIهای مالی لحظه‌ای و ماژول احراز هویت دومرحله‌ای اختصاصی پیاده‌سازی گردید.',
            client_name='هلدینگ آریا',
            technologies='Django, HTMX, TailwindCSS, PostgreSQL',
            website_url='https://example.com',
            is_published=True,
            is_featured=True,
            order=1
        )
        Project.objects.create(
            title='فروشگاه آنلاین تخصصی نوین تک',
            slug='novintech-store',
            category=c_shop,
            short_description='فروشگاه اینترنتی فروش قطعات سخت‌افزاری با فیلتر هوشمند مشخصات و درگاه مستقیم بانکی.',
            description='پیاده‌سازی سبد خرید بلادرنگ با Alpine.js، جستجوی آنی محصولات، محاسبه داینامیک هزینه ارسال و اتصال به درگاه شاپرک.',
            client_name='بازرگانی نوین تک',
            technologies='Python, Django, Redis, TailwindCSS',
            website_url='https://example.com',
            is_published=True,
            is_featured=True,
            order=2
        )
        Project.objects.create(
            title='سامانه نوبت‌دهی آنلاین کلینیک مهر',
            slug='mehr-clinic',
            category=c_serv,
            short_description='سامانه رزرو وقت آنلاین پزشکان با تقویم شمسی هوشمند و ارسال پیامک یادآوری خودکار.',
            description='سامانه‌ای واکنش‌گرا برای بیماران و منشی کلینیک با قابلیت انتخاب پزشک، تاریخ، ساعت خالی و پرداخت بیعانه.',
            client_name='کلینیک تخصصی مهر',
            technologies='Django, Celery, SMS Gateway, Alpine.js',
            website_url='https://example.com',
            is_published=True,
            is_featured=True,
            order=3
        )
        Project.objects.create(
            title='وب‌سایت بین‌المللی شرکت پتروپارس',
            slug='petropars-co',
            category=c_corp,
            short_description='پرتال شرکتی چندزبانه (فارسی و انگلیسی) برای شرکت صادراتی فعال در حوزه پتروشیمی.',
            description='طراحی مدرن با کاتالوگ دیجیتال محصولات، فرم‌های درخواست همکاری و صفحات بهینه‌سازی شده برای مخاطبان خارجی.',
            client_name='شرکت بازرگانی پتروپارس',
            technologies='Django, i18n, TailwindCSS',
            website_url='https://example.com',
            is_published=True,
            is_featured=False,
            order=4
        )
        self.stdout.write('[OK] Portfolio seeded.')

        # 5. Pricing Calculator Categories & Modules (Matching bamboweb.ir)
        PricingCategory.objects.all().delete()
        cat_infra = PricingCategory.objects.create(name='زیرساخت و سرور', icon='server', order=1)
        cat_design = PricingCategory.objects.create(name='طراحی و ظاهر', icon='palette', order=2)
        cat_content = PricingCategory.objects.create(name='امکانات محتوایی', icon='document', order=3)
        cat_sales = PricingCategory.objects.create(name='فروش و تعاملات', icon='shopping-cart', order=4)
        cat_seo = PricingCategory.objects.create(name='سئو و بهینه‌سازی', icon='chart-bar', order=5)
        cat_sec = PricingCategory.objects.create(name='امنیت و پشتیبانی', icon='shield-check', order=6)

        PricingModule.objects.all().delete()
        # Infrastructure
        m_host = PricingModule.objects.create(category=cat_infra, name='هاست ابری پرسرعت یک‌ساله', price=2500000, is_default=True, is_required=True, order=1)
        m_resp = PricingModule.objects.create(category=cat_infra, name='طراحی ریسپانسیو موبایل و تبلت', price=3000000, is_default=True, is_required=True, order=2)
        m_pwa = PricingModule.objects.create(category=cat_infra, name='نسخه وب‌اپلیکیشن (PWA)', price=4500000, is_default=False, order=3)
        m_multi = PricingModule.objects.create(category=cat_infra, name='قابلیت دوزبانه (فارسی/انگلیسی)', price=5000000, is_default=False, order=4)

        # Design
        m_cust_design = PricingModule.objects.create(category=cat_design, name='طراحی گرافیکی اختصاصی در فیگما', price=6000000, is_default=True, order=1)
        m_logo = PricingModule.objects.create(category=cat_design, name='طراحی لوگو و هویت بصری', price=4000000, is_default=False, order=2)
        m_dark = PricingModule.objects.create(category=cat_design, name='پشتیبانی از حالت تیره (Dark Mode)', price=2000000, is_default=True, order=3)
        m_anim = PricingModule.objects.create(category=cat_design, name='انیمیشن‌های مدرن اسکرول و مایکرو اینتراکشن', price=3000000, is_default=False, order=4)

        # Content
        m_blog = PricingModule.objects.create(category=cat_content, name='سیستم وبلاگ و انتشار مقالات آموزشی', price=2500000, is_default=True, order=1)
        m_gallery = PricingModule.objects.create(category=cat_content, name='گالری تصاویر و ویدئو با لایت‌باکس', price=1500000, is_default=False, order=2)
        m_custom_form = PricingModule.objects.create(category=cat_content, name='فرم‌ساز سفارشی و پرسش‌نامه آنلاین', price=2000000, is_default=False, order=3)
        m_user_panel = PricingModule.objects.create(category=cat_content, name='پنل کاربری اختصاصی اعضا', price=6500000, is_default=False, order=4)

        # Sales
        m_gateway = PricingModule.objects.create(category=cat_sales, name='اتصال به درگاه پرداخت آنلاین بانکی', price=3500000, is_default=False, order=1)
        m_booking = PricingModule.objects.create(category=cat_sales, name='سیستم رزرواسیون و نوبت‌دهی هوشمند', price=5500000, is_default=False, order=2)

        # SEO
        m_tech_seo = PricingModule.objects.create(category=cat_seo, name='سئو تکنیکال و استانداردسازی کدها', price=3500000, is_default=True, order=1)
        m_gsc = PricingModule.objects.create(category=cat_seo, name='اتصال به Google Search Console و ثبت نقشه', price=1500000, is_default=True, order=2)
        m_speed = PricingModule.objects.create(category=cat_seo, name='بهینه‌سازی سرعت و امتیاز PageSpeed بالای ۹۰', price=3000000, is_default=False, order=3)

        # Security
        m_ssl = PricingModule.objects.create(category=cat_sec, name='نصب و کانفیگ گواهی امنیتی SSL', price=1000000, is_default=True, is_required=True, order=1)
        m_backup = PricingModule.objects.create(category=cat_sec, name='سیستم پشتیبان‌گیری خودکار روزانه ابری', price=2500000, is_default=True, order=2)
        m_2fa = PricingModule.objects.create(category=cat_sec, name='ورود دو مرحله‌ای ادمین (2FA)', price=2000000, is_default=False, order=3)
        m_chat = PricingModule.objects.create(category=cat_sec, name='سیستم گفتگوی آنلاین و پشتیبانی چت', price=1800000, is_default=False, order=4)

        # Presets
        PricingPreset.objects.all().delete()
        p1 = PricingPreset.objects.create(
            name='پکیج پایه شرکتی',
            slug='basic-corporate',
            description='مناسب کسب‌وکارهای نوپا برای معرفی رسمی خدمات و محصولات',
            order=1
        )
        p1.modules.set([m_host, m_resp, m_cust_design, m_dark, m_blog, m_tech_seo, m_gsc, m_ssl, m_backup])

        p2 = PricingPreset.objects.create(
            name='پکیج پیشرفته خدماتی',
            slug='advanced-service',
            description='پکیج کامل با سیستم رزرواسیون و انیمیشن‌های حرفه‌ای',
            order=2
        )
        p2.modules.set([m_host, m_resp, m_cust_design, m_dark, m_anim, m_blog, m_gallery, m_booking, m_tech_seo, m_gsc, m_speed, m_ssl, m_backup, m_chat])

        p3 = PricingPreset.objects.create(
            name='پکیج جامع تجاری / فروشگاهی',
            slug='enterprise-store',
            description='بالاترین سطح امکانات با درگاه پرداخت، PWA و پنل کاربری',
            order=3
        )
        p3.modules.set([m_host, m_resp, m_pwa, m_cust_design, m_logo, m_dark, m_anim, m_blog, m_gallery, m_user_panel, m_gateway, m_tech_seo, m_gsc, m_speed, m_ssl, m_backup, m_2fa, m_chat])
        self.stdout.write('[OK] Pricing modules & presets seeded.')

        # 6. Blog Articles
        ArticleCategory.objects.all().delete()
        b_cat1 = ArticleCategory.objects.create(name='طراحی و توسعه وب', slug='web-design', order=1)
        b_cat2 = ArticleCategory.objects.create(name='سئو و بهینه‌سازی', slug='seo', order=2)
        b_cat3 = ArticleCategory.objects.create(name='کسب‌وکار دیجیتال', slug='digital-business', order=3)

        Article.objects.all().delete()
        a1 = Article.objects.create(
            title='چرا سرعت وب‌سایت مهم‌ترین فاکتور فروش در سال ۲۰۲۶ است؟',
            slug='why-website-speed-matters',
            category=b_cat1,
            excerpt='هر یک ثانیه تاخیر در بارگذاری وب‌سایت، نرخ تبدیل مشتریان را تا ۲۰ درصد کاهش می‌دهد. در این مقاله به بررسی راهکارهای عملی بهبود سرعت می‌پردازیم.',
            content='سرعت وب‌سایت یکی از کلیدی‌ترین ارکان تجربه کاربری و سئو در وب مدرن است. موتورهای جستجو مانند گوگل سایت‌هایی را در نتایج برتر قرار می‌دهند که زمان پاسخگویی سرور (TTFB) زیر ۲۰۰ میلی‌ثانیه و لود کلی زیر ۱ ثانیه داشته باشند.\n\nاستفاده از معماری بهینه جنگو، تبدیل خودکار تصاویر به WebP و کشینگ با Redis از جمله مهم‌ترین تکنیک‌هایی است که ما در تک سرویس به کار می‌گیریم.',
            author_name='مهندس رضایی',
            is_published=True,
            published_at=timezone.now(),
            reading_time=4
        )
        a1.tags.add('سرعت سایت', 'سئو', 'توسعه وب')

        a2 = Article.objects.create(
            title='تفاوت وب‌سایت کدنویسی اختصاصی در مقابل وردپرس: کدام برای شما مناسب‌تر است؟',
            slug='custom-code-vs-wordpress',
            category=b_cat3,
            excerpt='مقایسه کامل امنیت، سرعت، انعطاف‌پذیری و هزینه‌های نگهداری سایت اختصاصی با سیستم‌های آماده.',
            content='سیستم‌های آماده مانند وردپرس برای وبلاگ‌های ساده کارآمد هستند، اما با افزایش تعداد افزونه‌ها با افت شدید سرعت و خطرات امنیتی مواجه می‌شوند.\n\nتوسعه اختصاصی با Django امنیت در سطح بانکی، کنترل صددرصدی روی سورس کد و امکان افزودن هرگونه ماژول دلخواه بدون محدودیت را فراهم می‌آورد.',
            author_name='تیم فنی تک سرویس',
            is_published=True,
            published_at=timezone.now(),
            reading_time=6
        )
        a2.tags.add('جنگو', 'وردپرس', 'برنامه‌نویسی')

        a3 = Article.objects.create(
            title='چک‌لیست طلایی سئوی تکنیکال برای راه‌اندازی وب‌سایت جدید',
            slug='technical-seo-checklist',
            category=b_cat2,
            excerpt='نکات حیاتی درباره متاتگ‌ها، نشانی‌های استاندارد Canonical، نقشه سایت Sitemap و داده‌های ساختاریافته Schema.',
            content='پیش از عمومی‌سازی هر وب‌سایت جدید، رعایت اصول سئوی فنی ضروری است. در این چک‌لیست گام‌های پیکربندی Robots.txt، Sitemaps XML داینامیک و متاتگ‌های شبکه‌های اجتماعی Open Graph تشریح شده‌اند.',
            author_name='کارشناس سئو',
            is_published=True,
            published_at=timezone.now(),
            reading_time=5
        )
        a3.tags.add('سئو تکنیکال', 'گوگل')
        self.stdout.write('[OK] Blog seeded.')

        # 7. Testimonials
        Testimonial.objects.all().delete()
        Testimonial.objects.create(
            name='مهندس کیانی',
            company='مدیرعامل هلدینگ آریا',
            role='کارفرما',
            content='سرعت تحویل پروژه و طراحی تمیز و مدرن تک سرویس فراتر از انتظار ما بود. ماشین حساب قیمت آن‌ها دقیقا همان رقمی را برآورد کرد که در قرارداد منعقد شد.',
            rating=5,
            is_active=True,
            order=1
        )
        Testimonial.objects.create(
            name='دکتر صادقی',
            company='کلینیک تخصصی مهر',
            role='پزشک و موسس',
            content='سیستم نوبت‌دهی آنلاین طراحی شده بسیار روان و بی‌دردسر است و بار کاری منشی‌های مطب را به طور چشمگیری کاهش داده است.',
            rating=5,
            is_active=True,
            order=2
        )
        Testimonial.objects.create(
            name='خانم مهندس عباسی',
            company='فروشگاه نوین تک',
            role='مدیر فروش دیجیتال',
            content='پشتیبانی عالی و پیگیری مستمر تیم تا اطمینان از عملکرد درست درگاه پرداخت و فرآیندها تحسین‌برانگیز بود.',
            rating=5,
            is_active=True,
            order=3
        )
        self.stdout.write('[OK] Testimonials seeded.')

        # 8. About & Stats
        CompanyStat.objects.all().delete()
        CompanyStat.objects.create(title='پروژه موفق', value='+۴۵', order=1)
        CompanyStat.objects.create(title='رضایت مشتریان', value='۹۹٪', order=2)
        CompanyStat.objects.create(title='سال تجربه تخصصی', value='۶+', order=3)
        CompanyStat.objects.create(title='ساعت پشتیبانی فعال', value='۲۴/۷', order=4)

        TeamMember.objects.all().delete()
        TeamMember.objects.create(name='علیرضا محمدی', role='مدیر ارشد فنی و معمار نرم‌افزار', bio='متخصص توسعه بک‌اند با ۱۰ سال سابقه در معماری سیستم‌های پرسرعت Django و دیتابیس‌های مقیاس‌پذیر.', experience_years=10, order=1)
        TeamMember.objects.create(name='سارا کریمی', role='طراح ارشد رابط کاربری (UI/UX)', bio='طراح باسابقه متمرکز بر ساخت طراحی‌های مدرن دارک‌مود، سیستم‌های دیزاین و خلق تجربه کاربری تعاملی.', experience_years=7, order=2)
        TeamMember.objects.create(name='حسین ابراهیمی', role='توسعه‌دهنده فرانت‌اند', bio='متخصص تکنولوژی‌های وب، سرعت لود و استانداردهای بهینه‌سازی CSS و JS.', experience_years=5, order=3)
        TeamMember.objects.create(name='نیلوفر راد', role='متخصص سئو و استراتژی محتوا', bio='متمرکز بر رشد ترافیک ارگانیک، سئو تکنیکال و استراتژی بازاریابی دیجیتال.', experience_years=6, order=4)
        self.stdout.write('[OK] About & Stats seeded.')

        self.stdout.write(self.style.SUCCESS('All data seeded successfully!'))

