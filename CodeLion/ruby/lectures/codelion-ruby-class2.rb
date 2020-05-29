# # declaring a function
# def make_dolcelatte
#     puts "1. 얼음을 넣는다."
#     puts "2. 연유를 30ml 넣는다."
#     puts "3. 찬 우유를 넣는다."
#     puts "4. 에스프레소 샷을 넣는다."
# end


# making a global variable -- @variable
@x = []
@x << "a"
@x << "b"
@x << "c"

def print_x
    puts @x.inspect
end

print_x