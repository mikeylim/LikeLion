###### 1st way
pairs = {"한국"=>"서울","베트남"=>"하노이","미국"=>"워싱턴"}
# while loop
loop do
    # pairs의 사이즈가 0이 아니면 퀴즈를 계속해라!
    if pairs.size == 0
        puts "문제를 모두 맞추셨습니다. 열심히 공부 하셨군요~ ^_^"
        break
    else
        pairs.each do |country, capital|
            puts "#{country} 의 수도를 맞추세요 : "
            answer = gets.chomp
            if (answer == capital)
                puts "정 답 입니다!"
                pairs.delete(country)
            else
                puts "땡! 틀렸습니다. #{country} 의 수도는 [#{capital}] 입니다."
            end
        end
        puts "모든 질문이 끝났습니다. 오답을 묶어서 다시 시작합니다."
    end
end

# ###### 2nd way
# pairs = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# # while loop
# loop do
#     pairs.each do |country, capital|
#         puts "#{country} 의 수도를 맞추세요 : "
#         answer = gets.chomp
#         if (answer == capital)
#             puts "정 답 ----- #{country} 의 수도는 #{capital} 가 맞습니다."
#             pairs.delete(country)
#         else
#             puts "땡! 틀렸습니다. #{country} 의 수도는 #{capital} 입니다."
#         end
#     end
#     # pairs의 사이즈가 0이면 loop를 멈춰라!
#     if pairs.size == 0
#         break
#     end
#     puts "모든 질문이 끝났습니다. 오답을 묶어서 다시 시작합니다."
# end