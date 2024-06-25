# nambazasimu

A Python package that identifies a Tanzanian phone number with respect to the mobile network (carrier).

## Why is this important?

In Tanzania, it can be challenging to identify which mobile network a phone number belongs to. This can be especially important for various services that rely on knowing the carrier, such as billing, sending cash, customer support, or mobile-specific features.

## Mobile Networks covered  
- [x] Vodacom
- [x] Tigo
- [x] Airtel
- [x] Halotel
- [x] Zantel
- [x] Smile

## Research

The author conducted intensive research and came across useful resources:

- [Wikipedia article on Tanzanian phone numbers](https://sw.wikipedia.org/wiki/Namba_za_simu_Tanzania)
- [Wikipedia article on Telephone numbers in Tanzania](https://en.m.wikipedia.org/wiki/Telephone_numbers_in_Tanzania)
- [Jamii Forums thread on identifying phone numbers by network](https://www.jamiiforums.com/threads/jinsi-ya-kutambua-namba-ya-simu-ni-ya-mtandao-upi.1438096/)

## Installation

You can install the `nambazasimu` package via pip:

```bash
pip install nambazasimu
```

## Usage

To use the package, you can import the `identify_carrier` function and pass a Tanzanian phone number to it. Here's a simple example:

```python
from nambazasimu.carrier_identifier import identify_carrier

print(identify_carrier("+255684567890"))  # Output: Airtel
print(identify_carrier("255754567890"))   # Output: Voda
print(identify_carrier("0714567890"))     # Output: Tigo
```

## How to Contribute

If you'd like to contribute to this project, follow these steps:

1. **Fork the repo**: Click the "Fork" button at the top right of the repository page.
2. **Clone the forked repo**: 

    ```bash
    git clone https://github.com/<yourusername>/nambazasimu.git
    ```
3. **Navigate to the project directory**:

    ```bash
    cd nambazasimu
    ```
4. **Set up a Python environment** and install the requirements:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
5. **Make your changes**, and be sure to write tests if necessary.
6. **Commit your changes**:

    ```bash
    git add .
    git commit -m "Description of your changes"
    ```
7. **Push your changes to your fork**:

    ```bash
    git push origin your-branch-name
    ```
8. **Raise a Pull Request**: Go to the original repository and create a new pull request.

##  Challenges

This package won't work if a phone number has undergone **Mobile Number Portability** .

### What is MNP ( Mobile Number Portability ) ?

Mobile Number Portability (MNP) is a telecommunications feature that allows mobile phone users to retain their phone numbers when switching from one mobile network operator to another.

## Raising Issues

If you encounter any issues, please report them via the [GitHub issues page](https://github.com/genie360s/nambazasimu/issues). Provide as much detail as possible about the issue, including any error messages and steps to reproduce the problem.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## References

- [Wikipedia article on Tanzanian phone numbers](https://sw.wikipedia.org/wiki/Namba_za_simu_Tanzania)
- [Wikipedia article on Telephone numbers in Tanzania](https://en.m.wikipedia.org/wiki/Telephone_numbers_in_Tanzania)
- [Jamii Forums thread on identifying phone numbers by network](https://www.jamiiforums.com/threads/jinsi-ya-kutambua-namba-ya-simu-ni-ya-mtandao-upi.1438096/)




## Example Code

Here are some more examples of how to use the package:

```python
from nambazasimu.carrier_identifier import identify_carrier

print(identify_carrier("+255625567890"))  # Output: Halotel
print(identify_carrier("255774567890"))   # Output: Zantel
print(identify_carrier("0734567890"))     # Output: TTCL
print(identify_carrier("+255123456789"))  # Output: Unknown
```

Feel free to reach out if you have any questions or need further assistance!

Author: Alex Mkwizu
Email : alexgmkwizu@gmail.com | @genie360s
