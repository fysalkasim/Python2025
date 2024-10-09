def data_science(*tools):
    for i in tools:
        print(f"I am using {i} for my data analaysis works")

def completed_calss(thislist):
    processed_orders = []
    while thislist:
        present_order = thislist.pop(0)
        print("processing=",present_order)
        processed_orders.append(present_order)