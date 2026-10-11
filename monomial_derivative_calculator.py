from sympy import ff, factorial
import math
from fractions import Fraction
import sys
sys.set_int_max_str_digits(250000)
# This function calculates monomial derivatives for numbers with positive integer powers
def derivative(coefficient, v_power, d_power):
    if coefficient == 0 and v_power == 0 and d_power == 0:
        print(f"Error! Please enter valid values aside from 0.")
        return
    elif coefficient == 0 or v_power == 0 or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return
    if d_power > v_power:
        print(f"The derivative of the monomial {coefficient}x^{v_power} at the derivative power of {d_power} is 0.")
        return
    
    falling_factorial_result = ff(v_power, d_power)
    new_coefficient = coefficient * falling_factorial_result
    new_exponent = v_power - d_power
    factorial_of_v_power = factorial(v_power)
    constant = coefficient * factorial_of_v_power

    if d_power == v_power:
        print(f"The derivative of the monomial {coefficient}x^{v_power} at the derivative power of {d_power} is {constant}.")
    elif d_power == v_power - 1:
            print(f"The derivative of the monomial {coefficient}x^{v_power} at the derivative power of {d_power} is {new_coefficient}x.")
    elif d_power < v_power:
        print(f"The derivative of the monomial {coefficient}x^{v_power} at the derivative power of {d_power} is {new_coefficient}x^{new_exponent}.")

# This function calculates monomial derivatives with a positive fractional coefficient
def derivative_pos_fractional_coefficient(c_numerator, c_denominator, v_power, d_power):
    if (c_numerator == 0 and c_denominator == 0) and v_power == 0 and d_power == 0:
        print(f"Error! Please enter valid values aside from 0.")
        return
    elif (c_numerator == 0 and c_denominator) or v_power == 0 or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return
    if d_power > v_power:
        print(f"The derivative of the monomial ({c_numerator}/{c_denominator})x^{v_power} at the derivative power of {d_power} is 0.")
        return
    
    falling_factorial_result = ff(v_power, d_power)
    coefficient = Fraction(c_numerator, c_denominator)
    new_coefficient = coefficient * falling_factorial_result
    new_exponent = v_power - d_power
    factorial_of_v_power = factorial(v_power)
    constant = coefficient * factorial_of_v_power

    if d_power == v_power:
        print(f"The derivative of the monomial ({coefficient})x^{v_power} at the derivative power of {d_power} is {constant}.")
    elif d_power == v_power - 1:
        print(f"The derivative of the monomial ({coefficient})x^{v_power} at the derivative power of {d_power} is ({new_coefficient})x.")
    elif d_power < v_power:
        print(f"The derivative of the monomial ({coefficient})x^{v_power} at the derivative power of {d_power} is ({new_coefficient})x^{new_exponent}.")

# This function calculates monomial derivatives for all fractional powers
def derivative_fractional_power_coefficient_not_fraction(coefficient, numerator, denominator, d_power):
    if coefficient == 0 and (numerator == 0 and denominator == 0) and d_power == 0:
         print(f"Error! Please enter valid values aside from 0.")
         return
    elif (coefficient == 0 and numerator == 0) or (denominator == 0 and d_power == 0):
             print(f"Error! Please enter valid values aside from 0.")
             return
    elif coefficient == 0 or (numerator == 0 and denominator == 0) or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return
    
    power = Fraction(numerator, denominator)
    fractional_d_power = Fraction(d_power, 1)
    coefficient_multiplier = ff(power, d_power)
    new_coefficient = coefficient_multiplier * coefficient
    new_exponent = power - fractional_d_power

    if d_power > 0 and d_power != 1 and coefficient == 1:
        print(f"The derivative of the monomial {coefficient}x^{power} at the derivative power of {d_power} is ({new_coefficient})x^({new_exponent})")

    elif d_power == 1 and coefficient == 1:
        print(f"The first derivative of the monomial x^({power}) is ({new_coefficient})x^({new_exponent}).")
    elif d_power == 1:
        print(f"The first derivative of the monomial {coefficient}x^({power}) is ({new_coefficient})x^({new_exponent}).")

    else:
        print(f"The derivative of the monomial {coefficient}x^({power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_exponent})")

# This function calculates monomial derivatives for all fractional powers and coefficients
def derivative_fractional_power_coefficient_fraction(c_numerator, c_denominator, numerator, denominator, d_power):
    if (c_numerator == 0 and c_denominator == 0) and (numerator == 0 and denominator == 0) and d_power == 0:
         print(f"Error! Please enter valid values aside from 0.")
         return
    elif (c_numerator == 0 and c_denominator == 0) and (numerator == 0 or denominator == 0) and d_power == 0:
             print(f"Error! Please enter valid values aside from 0.")
             return
    elif (c_numerator == 0 and c_denominator == 0) or (numerator == 0 and denominator == 0) or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return

    coefficient = Fraction(c_numerator, c_denominator)
    power = Fraction(numerator, denominator)
    fractional_d_power = Fraction(d_power, 1)
    coefficient_multiplier = ff(power, d_power)
    new_coefficient = coefficient_multiplier * coefficient
    new_exponent = power - fractional_d_power

    if d_power > 0 and d_power != 1 and coefficient == 1:
        print(f"The derivative of the monomial ({coefficient})x^{power} at the derivative power of {d_power} is ({new_coefficient})x^({new_exponent})")

    elif d_power == 1 and coefficient == 1:
        print(f"The first derivative of the monomial x^({power}) is ({new_coefficient})x^({new_exponent}).")
    elif d_power == 1:
        print(f"The first derivative of the monomial ({coefficient})x^({power}) is ({new_coefficient})x^({new_exponent}).")

    else:
        print(f"The derivative of the monomial ({coefficient})x^({power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_exponent})")

# This function calculates monomial derivatives for negative powers
def derivative_neg(coefficient, v_power, d_power):
    if coefficient == 0 and v_power == 0 and d_power == 0:
        print(f"Error! Please enter valid values aside from 0.")
        return
    elif coefficient == 0 or v_power == 0 or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return
    falling_factorial_result = ff(v_power, d_power)
    new_coefficient = coefficient * falling_factorial_result
    new_power = v_power - d_power

    if coefficient == 1:
        print(f"The derivative of the monomial x^({v_power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_power}).")
    else:
        print(f"The derivative of the monomial {coefficient}x^({v_power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_power}).")

# This function calculates monomial derivatives for negative powers with fractional coefficients
def derivative_neg_fractional_coefficients(c_numerator, c_denominator, v_power, d_power):
    if (c_numerator == 0 and c_denominator == 0) and v_power == 0 and d_power == 0:
             print(f"Error! Please enter valid values aside from 0.")
             return
    elif (c_numerator == 0 and c_denominator) or v_power == 0 or d_power == 0:
        print(f"Error! Please enter a valid value aside from 0.")
        return
    falling_factorial_result = ff(v_power, d_power)
    coefficient = Fraction(c_numerator, c_denominator)
    new_coefficient = coefficient * falling_factorial_result
    new_power = v_power - d_power

    if (c_numerator == 1 and c_denominator == 1):
        print(f"The derivative of the monomial x^({v_power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_power}).")
    else:
        print(f"The derivative of the monomial ({coefficient})x^({v_power}) at the derivative power of {d_power} is ({new_coefficient})x^({new_power}).")


print("============================-----------------------------------------------------------------------------")
print("Monomial (d/dx) when: No fractions or negative powers are present")
print()

# Replace 0 with all the values you want for the coefficient, variable power, and derivative power
# The variable is automatically x
# If your derivative power > variable power, the answer is 0
# Template for calling the function: derivative(0,0,0)
# Finally, I implore you to enter your values in this order: coefficient, variable power (must be positive), derivative power
derivative(0,0,0)
derivative(0,0,0)
derivative(0,0,0)

print("============================-----------------------------------------------------------------------------")
print("Monomial (d/dx) when: Coefficient is fractional with fractional powers")
print()

# Replace 0 with all the values you want for the coefficient, variable power numerator and denominator, and derivative power
# The variable is automatically x
# Template for calling the function: derivative_pos_fractional_coefficient(0,0,0,0)
# I implore you to enter your values in this order: coefficient power numerator, coefficient power denominator, variable power (must be positive), and derivative power
# Finally, I implore you not to do anything stupid like input a coefficient where it just simplifies to a whole number, there is another function for that
derivative_pos_fractional_coefficient(0,0,0,0)
derivative_pos_fractional_coefficient(0,0,0,0)
derivative_pos_fractional_coefficient(0,0,0,0)

print("============================-----------------------------------------------------------------------------")
print("Monomial (d/dx) when: Coefficient is not a fraction and is positive with a fractional power")
print()

# Replace 0 with all the values you want for the coefficient, variable power numerator and denominator, and derivative power
# The variable is automatically x
# Template for calling the function: derivative_fractional_power_coefficient_not_fraction(0,0,0,0)
# I implore you to enter your values in this order: coefficient, variable power numerator, variable power denominator and derivative power
# If you want a negative fraction make either the second or third value have a minus sign in front of it
# Finally, I implore you not to do anything stupid like input a power where it just simplifies to a whole number, there is another function for that
derivative_fractional_power_coefficient_not_fraction(0,0,0,0)
derivative_fractional_power_coefficient_not_fraction(0,0,0,0)
derivative_fractional_power_coefficient_not_fraction(0,0,0,0)

print("============================-----------------------------------------------------------------------------")
print("Monomial (d/dx) when: Coefficient is fractional with fractional powers")
print()

# Replace 0 with all the values you want for the coefficient, variable power numerator and denominator, and derivative power
# The variable is automatically x
# Template for calling the function: derivative_fractional_power_coefficient_fraction(0,0,0,0,0)
# I implore you to enter your values in this order: coefficient numerator, coefficient denominator, variable power numerator, variable power denominator, and derivative power
# Finally, I implore you not to do anything stupid like input a coefficient where it just simplifies to a whole number, there is another function for that
derivative_fractional_power_coefficient_fraction(0,0,0,0,0)
derivative_fractional_power_coefficient_fraction(0,0,0,0,0)
derivative_fractional_power_coefficient_fraction(0,0,0,0,0)


print("============================-----------------------------------------------------------------------------")
print("Monomial (d/dx) when: No fractions, negative powers")
print()

# Replace 0 with all the values you want for the coefficient, variable power, and derivative power
# The variable is automatically x
# Template for calling the function: derivative_neg(0,0,0)
# I implore you to enter your values in this order: coefficient, variable power (must be negative), and derivative power
# Because this is negative, the variable power has to have a minus sign
derivative_neg(0,0,0)
derivative_neg(0,0,0)
derivative_neg(0,0,0)

print("============================-----------------------------------------------------------------------------")
# Replace 0 with all the values you want for the coefficient numerator and denominator, variable power, and derivative power
# The variable is automatically x
# Template for calling the function: derivative_neg_fractional_coefficients(0,0,0,0)
# I implore you to enter your values in this order: coefficient numerator, coefficient denominator, variable power (must be negative), and derivative power
# Because this is negative, the variable power has to have a minus sign
derivative_neg_fractional_coefficients(0,0,0,0)
derivative_neg_fractional_coefficients(0,0,0,0)
derivative_neg_fractional_coefficients(0,0,0,0)

print("============================-----------------------------------------------------------------------------")
print("Thank you for using this calculator!")
print("============================-----------------------------------------------------------------------------")
print("- Brought to you by someone who also finds calculus hard |")
print("============================------------------------------")