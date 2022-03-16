discount_rate = .1
alpha = .1
while discount_rate < 1:
    s = "Discount Rate: {:.1f}, Alpha: {:.1f}".format(discount_rate, alpha)
    alpha_string = "{:.1f}".format(round(alpha,1))
    discount_string = "{:.1f}".format(round(discount_rate,1))
    
    database_name = "TD_Database_alpha_{}_discount_{}.pickle".format(alpha_string,discount_string)
    print(database_name)
    discount_rate += .1
    discount_rate = round(discount_rate,1)
    