# Here's an example program that uses **kwargs to generate the desired list of concatenations:

def concat_months(**kwargs):
    months = kwargs.get('months')
    days = kwargs.get('days')
    #concatenated = [f"{month}.{day}" for month, day in zip(months, days)]
    concatenated = [f"{months[i]}.{days[i]}" for i in range(len(months))]
    return concatenated

A = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
B = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

X = concat_months(months=A, days=B)
print(X)