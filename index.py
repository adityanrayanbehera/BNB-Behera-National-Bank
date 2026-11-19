
import streamlit as st

# -----------------------------------------
# PAGE SETTINGS
# -----------------------------------------

st.set_page_config(
    page_title="BNB – Behera National Bank",
    page_icon="🏦",
    layout="centered"
)

# -----------------------------------------
# CUSTOM DESIGN
# -----------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef4ff, #f8fbff);
}

.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* BANK HEADER */

.bank-header {
    background: linear-gradient(135deg, #061a40, #0b5ed7, #00a6ff);
    padding: 35px 20px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 10px 30px rgba(0, 80, 180, 0.25);
    margin-bottom: 25px;
}

.bank-logo {
    font-size: 55px;
}

.bank-name {
    font-size: 34px;
    font-weight: 800;
    letter-spacing: 2px;
    color: white;
}

.tagline {
    font-size: 16px;
    margin-top: 8px;
    color: white;
}

/* WELCOME CARD */

.welcome-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border-left: 6px solid #0b5ed7;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
    color: #333;
}

.welcome-title {
    font-size: 23px;
    font-weight: bold;
    color: #061a40;
}

.welcome-card p {
    font-size: 16px;
    color: #444;
    margin-bottom: 0;
}

/* BALANCE CARD */

.balance-card {
    background: linear-gradient(135deg, #071d49, #123d8d);
    padding: 25px;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    margin: 20px 0;
}

.balance-label {
    font-size: 16px;
    color: white;
}

.balance-value {
    font-size: 35px;
    font-weight: bold;
    margin-top: 5px;
    color: white;
}

/* DAY TITLE */

.day-title {
    background: white;
    padding: 12px 18px;
    border-radius: 14px;
    font-size: 20px;
    font-weight: bold;
    color: #061a40;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.07);
    margin-top: 15px;
}

/* SUMMARY TITLE */

.summary-title {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #061a40;
    margin-top: 30px;
    margin-bottom: 20px;
}

/* FOOTER */

.footer {
    margin-top: 35px;
    padding: 22px;
    border-radius: 18px;
    background: #061a40;
    color: white;
    text-align: center;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# BANK HEADER
# -----------------------------------------

st.html("""
<div class="bank-header">

    <div class="bank-logo">🏦</div>

    <div class="bank-name">
        BNB – Behera National Bank
    </div>

    <div class="tagline">
        💙 Your Money • Your Future • Our Responsibility
    </div>

</div>
""")


# -----------------------------------------
# WELCOME SECTION
# -----------------------------------------

st.html("""
<div class="welcome-card">

    <div class="welcome-title">
        👋 Welcome to BNB – Behera National Bank
    </div>

    <p>
        Manage your daily deposits and withdrawals easily.
        Keep track of your account balance for 4 days.
    </p>

</div>
""")


# -----------------------------------------
# STARTING BALANCE
# -----------------------------------------

starting_balance = 1000.0

balance = starting_balance
total_deposit = 0.0
total_withdraw = 0.0


st.html("""
<div class="balance-card">

    <div class="balance-label">
        💰 Starting Account Balance
    </div>

    <div class="balance-value">
        ₹1,000.00
    </div>

</div>
""")


# -----------------------------------------
# DAILY TRANSACTIONS
# -----------------------------------------

st.subheader("📋 Daily Banking Transactions")

for day in range(1, 5):

    st.html(
        f'<div class="day-title">📅 Day {day}</div>'
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        deposit = st.number_input(
            "💵 Deposit Amount (₹)",
            min_value=0.0,
            step=100.0,
            key="deposit" + str(day)
        )

    with col2:

        withdraw = st.number_input(
            "💸 Withdrawal Amount (₹)",
            min_value=0.0,
            step=100.0,
            key="withdraw" + str(day)
        )

    # Add deposit first

    balance = balance + deposit

    total_deposit = total_deposit + deposit

    # Check withdrawal

    if withdraw > balance:

        st.error(
            f"❌ Insufficient balance on Day {day}! "
            "Withdrawal was not completed."
        )

        valid_withdraw = 0.0

    else:

        valid_withdraw = withdraw

    # Subtract withdrawal

    balance = balance - valid_withdraw

    total_withdraw = total_withdraw + valid_withdraw

    # Display daily balance

    st.success(
        f"💰 Day {day} Closing Balance: ₹{balance:,.2f}"
    )


# -----------------------------------------
# ACCOUNT SUMMARY
# -----------------------------------------

st.html("""
<div class="summary-title">
    📊 Account Summary
</div>
""")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="💵 Total Deposits",
        value=f"₹{total_deposit:,.2f}"
    )

with col2:

    st.metric(
        label="💸 Total Withdrawals",
        value=f"₹{total_withdraw:,.2f}"
    )

st.metric(
    label="🏦 FINAL ACCOUNT BALANCE",
    value=f"₹{balance:,.2f}"
)


# -----------------------------------------
# ACCOUNT STATUS
# -----------------------------------------

st.subheader("🏦 Account Status")

if balance >= 1000:

    st.success(
        "🟢 Account Status: Healthy — "
        "Your balance is ₹1,000 or above."
    )

else:

    st.warning(
        "🟠 Account Status: Low Balance — "
        "Your balance is below ₹1,000."
    )


# -----------------------------------------
# FOOTER
# -----------------------------------------

st.html("""
<div class="footer">

    🏦 <b>BNB – Behera National Bank</b>

    <br><br>

    🔐 Secure Banking &nbsp; | &nbsp;
    💰 Smart Savings &nbsp; | &nbsp;
    🤝 Trusted Service

    <br><br>

    <small>
        © 2026 BNB – Behera National Bank
        • All Rights Reserved
    </small>

</div>
""")
