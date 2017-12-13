- Why should we use functions?
Vì khi code, có những đoạn code có chức năng nhất định cần sử dụng nhiều lần, ngoài
ra đôi khi còn cần thay đổi số liệu, sử dụng functions dễ giúp code ngắn gọn, dễ đọc
hơn. Fuctions còn có thể dùng cho các file code khác.


- How to define/declare a function?
def functionname(parameters):
    function of the function
    #example: print('Something')


- How to call/use a function?
functionname(arguments)


- What is return, why and how do we use it?
Sau khi define xong function thì các biến trong function sẽ bị python tự động xóa bỏ.
Return được dùng để gửi điều khiển quay trở lại người gọi với một biến trong function,
nhờ vậy có thể sử dụng chúng ngoài function.


- Do we have to use return in every function?
Nope vì theo em đọc ở đâu đó thì nó không bắt buộc.


- What are function arguments/parameters, why and how we use it?
    Arguments là dữ liệu được truyền trong lời gọi hàm, nó có thể là hằng số, biến hay
biểu thức.
    Parameters là dữ liệu được nhận trong phần define function, nó bắt buộc phải là biến.
    Cách dùng:
def functionname(parameters):
    function of the function

functionname(arguments)

- How to use function from a different file other than our currently working file?
import function_file
function_file.functionname()

from function_file import functionname

from function_file import *
