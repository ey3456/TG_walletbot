# bot/keyboards.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💼 钱包", callback_data="wallet"),
         InlineKeyboardButton("📈 行情", callback_data="market")],
        [InlineKeyboardButton("📤 转账", callback_data="transfer"),
         InlineKeyboardButton("📜 历史", callback_data="history")],
        [InlineKeyboardButton("⚙️ 设置", callback_data="settings")]
    ])

def wallet_detail(currency: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 收款", callback_data=f"receive_{currency}"),
         InlineKeyboardButton("📤 转出", callback_data=f"send_{currency}")],
        [InlineKeyboardButton("🔙 返回", callback_data="main")]
    ])
