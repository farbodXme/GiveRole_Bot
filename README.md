# Discord Role Manager Bot
این بات برای مدیریت رول اعضای سرور دیسکورد شما طراحی شده است. با استفاده از این بات، می‌توانید به اعضا رول بدهید و بعد از مدت زمان مشخص، رول‌ها به صورت خودکار حذف شوند.

## ویژگی‌ها
حذف خودکار رول: رول را به یک عضو برای مدت معین اضافه کنید و بعد از آن مدت، نقش به طور خودکار حذف می‌شود.
پاسخ به پیام‌ها: بات به پیام‌های خاص از اعضایی که نقش معینی دارند پاسخ می‌دهد.
دستورات مدیریت نقش: ادمین‌ها می‌توانند نقش‌ها را به صورت دستی اضافه یا حذف کنند.
## دستورات
اضافه کردن رول:
``` !addrole @member @role روزها ```
  - مثال:
``` !addrole @user @role 7 ```
- حذف کردن نقش:
``` !removerole @member @role```

## Setup
- Clone the repository:

```git clone https://github.com/yourusername/discord-role-manager-bot.git ```

- Install dependencies:
`pip install discord.py`

- Configure the bot:

Replace `YOUR_BOT_TOKEN` with your bot's token.
Replace `ROLE_ID` with the ID of the role that the bot should respond to.

## Run the bot:
``` python bot.py ```

<img src="https://profile-counter.glitch.me/farbodXme/count.svg" alt="Visitors">
