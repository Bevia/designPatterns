# The Proxy Design Pattern is a structural pattern that provides an object that acts
# as a substitute or placeholder for another object. It controls access to the original object,
# allowing you to add functionality before or after the requests get to the original object.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."


class Proxy:
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        else:
            return "Proxy: Access denied."

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        # Simulate some access check logic
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


# Client code
def client_code(subject):
    # ...
    print(subject.request())
    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nClient: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

# Explanation:
# 1. RealSubject: This is the class representing the original object that performs some real operations.
# 2. Proxy: This class has a reference to the RealSubject and controls access to it. It can add additional functionality like access control and logging.
# 3. client_code: This function simulates the client code that interacts with the subject. It can interact with either the RealSubject directly or through the Proxy.
#
# When you run this code, you will see the following output:
#
# Client: Executing the client code with a real subject:
# RealSubject: Handling request.
#
# Client: Executing the same client code with a proxy:
# Proxy: Checking access prior to firing a real request.
# Proxy: Logging the time of request.
# RealSubject: Handling request.
#
# In this example, the `Proxy` class checks access before forwarding the request to the `RealSubject`
# and logs the access after the request. The client code remains the same and
# doesn('t need to change regardless of whether it is using a real subject or a proxy. '
#       'This demonstrates how the Proxy Pattern can control access to an object and add additional behavior without modifying the client code.)
