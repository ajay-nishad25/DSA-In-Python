"""
Excellent. This is the first topic where Python OOP differs significantly from Java.

If you come from Java, your biggest confusion will probably be:

"Where are public, private, and protected keywords?"

The answer is Python doesn't have real access modifiers like Java.

Let's understand the Pythonic way.

"""

"""
1. What is Encapsulation?

The definition is exactly the same as Java.

Encapsulation is the process of binding data (variables) and methods together into a single unit (a class) while controlling access to that data.

Its goals are:
Protect object data
Hide implementation details
Prevent accidental modification
Improve maintainability

====================
Java
class Student {

    private String name;

    public void setName(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }

}

Access is controlled using keywords.

====================

Python

Python has no keywords like:

private
protected
public

Instead, Python uses naming conventions.

Python Access Levels
Java	        Python
public	        Normal variable
protected	    _variable
private	        __variable

Notice:

Python uses underscores instead of keywords.
"""


# ======================= 2. Public Members

# Everything is public by default.

class Student:

    def __init__(self):
        self.name = "Ajay"
        self.age = 22


s = Student()

print(s.name)
print(s.age)

s.name = "Rahul"

print(s.name)

# Anyone can access or modify public members.

# ======================== 3. Protected Members

# python uses single underscore to represent protected variable or method 
# example

print("Protected Members example")

class ClassRoom:
    def __init__(self,name,marks):
        self._name = name
        self._marks = marks

    def print_student_details(self):
        print(self._name)
        print(self._marks)

    def _get_marks(self):
        print(self._marks)

class Students(ClassRoom):
    def __init__(self,name,marks):
        super().__init__(name,marks)

    def _get_student_details(self):
        super().print_student_details()

    # print("i am in Student class and i can access protected memeber(variable) i.e : ", super()._name)

s1 = Students("Ajay",100)
s2 = Students("Rahul",90)

print("i can still access the protected memeber from outside the class and subclass : ",s1._name)
print("i can still access the protected memeber from outside the class and subclass : ",s2._name)

s1._get_marks()
s2._get_marks()

s1._get_student_details()
s2._get_student_details()

"""
If you're coming from languages like Java, C++, or C#, this usually feels like a total shock! In those languages, 
the compiler strictly enforces the protected rule and throws an error if you try to access a protected member from outside the class hierarchy.

Python, however, operates on a very different philosophy: "We are all consenting adults here."

How "Protected" Works in Python
In Python, prefixing a variable or method with a single underscore (e.g., _my_variable) is purely a convention, not an access barrier.


Why Python does this
1. Developer Trust: Python assumes developers know what they are doing. The single underscore is a polite signpost saying: 
"Hey, this is an internal implementation detail. Touch it at your own risk because I might change or remove it in the future."

2. Dynamic Nature: Python prioritizes flexibility over strict encapsulation and compile-time access controls.
"""

# =========================== 4. Private Members

class Students:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

s = Students("Ajay",23)


# below direct access of private members result in no attribute error
# print(s.name)
# print(s.__marks)

# ====Name Mangling

"""
Internally,

Python changes

__name
__marks

into

_Student__name
_Student__marks

This process is called

Name Mangling
"""

# see here
print(vars(s))

"""
Accessing Private Members

Technically possible.

print(s._Student__name)
print(s._Student__marks)

Output
Ajay
23

Python doesn't make variables truly private.

It simply renames them.
Why?

Because Python follows

"We are all consenting adults here."

The language trusts programmers.
"""

print(s._Students__name)
print(s._Students__marks)

"""
Why Use Name Mangling?

Suppose

class Parent:

    def __show(self):
        print("Parent")


class Child(Parent):

    def __show(self):
        print("Child")

Without name mangling,

the child's method would overwrite the parent's method.

Instead,

Python stores them internally as

_Parent__show

_Child__show

No collision occurs.

NOTE: The real purpose of name mangling isn't privacy—it's safety in inheritance.

Imagine someone imports your BankAccount class and creates a child class called SavingsAccount. 
If both classes use a generic internal variable name like __id, name mangling ensures they don't overwrite each other:

class BankAccount:
    def __init__(self):
        self.__id = "BANK_123"  # Mangled to _BankAccount__id

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.__id = "SAVINGS_456"  # Mangled to _SavingsAccount__id

Because of mangling, both _BankAccount__id and _SavingsAccount__id exist peacefully in memory without clashing.
"""


# =========================== Getters and Setters 
"""
Now that you know private variables are meant to be protected inside a class, how do you let outside code read or change them safely?

That is where Getters and Setters come in.

Getter: A method that reads (gets) the value of a private attribute.

Setter: A method that updates (sets) the value of a private attribute—usually after validating that the new value is allowed.
"""

print("Example of setter and getters")

class Students:

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if len(name)<3 :
            print("Invalid name : ")
        else:
            self.__name = name

    def get_age(self):
        try:
            return self.__age
        except:
            print("Invalid age : ")


    def set_age(self,age):
        if age<=0 or age>=18:
            print("Invalid age : ")
            return
        else:
            self.__age = age

s1 = Students()
s1.set_name("Ajay")
s1.set_age(4)

print(s1.get_name())
print(s1.get_age())


# ======================= Private Methods

# Just like private variables, you make a method private by prefixing its name with double underscores (__).
# A Private Method is a helper function inside a class that is meant for internal use only. Outside code cannot call it directly; only other methods inside the same class should call it.

print("Private Methods Example")

class EmailService:
    def __init__(self,receipient,message):
        self.__receipient = receipient
        self.__message =  message

    def __connect_to_server(self):
        print("Connecting to secure SMTP server...")

    def __authenticate(self):
        print("Authenticating server credentials...")

    def send_email(self):
        self.__connect_to_server()
        self.__authenticate()
        print(f"Email sent to {self.__receipient} with message : {self.__message}")

email = EmailService("ajaynishad@gmail.com","Hello there!")

email.send_email() # call this non-private method which will eventually call the private methods 

# try to access private methods outside the class

try :
    email.__connect_to_server()
except Exception as e:
    print("\nError : ",e)
