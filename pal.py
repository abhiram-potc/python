def is_palindrome(n):
    n_str=str(n)
    n_rev=n[slice(None, None, -1)]
    if n_str==n_rev:
        print("The number ",n_rev," is palindrome")
    else:
        print("The number ",n_str," is not palindrome")
n=input("Enter digit: ")
is_palindrome(n)