def main():
    # use a for loop over a collection
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(Months):
        print(i, m)

if __name__ == "__main__":
    main()

# use the break and continue statements


for x in range (10,20):
    if (x == 15):
        break
    if (x % 5 == 0) :
        continue
    print (x)


