# bot/utils.py
def format_wallet_info(balance: float, currency: str, address: str) -> str:
    return (
        f"*📊 钱包详情*\n"
        f"├─ 币种: `{currency}`\n"
        f"├─ 余额: *{balance:.8f}* {currency}\n"
        f"├─ 地址: `{address}`\n"
        f"└─ 最近交易: [查看](https://explorer.example.com/tx/...)\n"
        f"\n_更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}_"
    )
