is_logged_in=True
is_subscribed=False

user_credits=100
max_credits=200
min_credits=50

credits_valid=(
    user_credits>=min_credits and
    user_credits<=max_credits and
    user_credits!=min_credits
)

bonus_eligible=is_subscribed or (user_credits>min_credits)and not is_subscribed

user_credits+=50
user_credits-=20
user_credits*=2
user_credits%=150

power_result=user_credits**2

full_access=is_logged_in and is_subscribed

is_true_loggin=is_logged_in is True

acces_result=is_logged_in or is_subscribed and False

print(is_logged_in)
print(is_subscribed)
print(credits_valid)
print(bonus_eligible)
print(user_credits)
print(power_result)
print(full_access)
print(is_true_loggin)
print(acces_result)