# # printing random value from list
# puts ['한국', '베트남', '미국'].sample

# # variable declaration in Ruby
# country_list = ['한국', '베트남', '미국']

# # while loop in Ruby
# loop do
#     puts ['한국', '베트남', '미국'].sample
#     sleep(1)
#     break
# end

# # for loop in ruby
# 1.upto(10) do # 1 and 30 are inclusive - 1 ~ 10 --> 10 // 0 ~ 10 --> 31
#     puts ['한국', '베트남', '미국'].sample
# end

# # data structure - hash (dictionary in python) object
# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# puts "한국 수도 - " + capitals["한국"]

# # adding value to list
# nations = ["한국", "베트남", "미국"]
# nations.push("프랑스")
# puts nations

# # deleting value from list
# nations = ["한국", "베트남", "미국"]
# nations.delete("미국")
# puts nations

# # adding key-value to hash
# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# capitals["프랑스"] = "파리"
# puts capitals

# # deleting key-value from hash
# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# capitals.delete("미국")
# puts capitals

# # length/size of hash
# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# numCapitals = capitals.size
# puts numCapitals

# # swapping key-value in hash
# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# puts capitals.invert

# # for loop storing value to x variable
# 1.upto(10) do |x|
#     puts x
# end

# nations = ["한국", "베트남", "미국"]
# numNations = nations.size

# 0.upto(numNations - 1) do |x|
#     puts "#{x} - #{nations[x]}"
# end

# # for ... each
# nations = ["한국", "베트남", "미국"]
# nations.each do |x|
#     puts x
# end

# capitals = {"한국" => "서울", "베트남" => "하노이", "미국" => "워싱턴"}
# capitals.each do |x,y|
#     puts x + " - " + y
# end

# # 만약에-If 그렇다면만약에-elsif 그렇지않다면-Else   **end is necessary in ruby
# nations = ["한국", "베트남", "미국"]
# randomNation = nations.sample 
# if (randomNation == "한국")
#     puts randomNation
#     puts "만세"
# elsif (randomNation == "미국")
#     puts randomNation
#     puts "USA!" 
# else
#     puts randomNation
#     puts "헬로우"
# end


# wating for user Input ---- gets.chomp
puts "비밀번호를 입력 해주세요"
answer = gets.chomp
answer = gets # samething, but in a new line, like \n answer
answer = gets.chomp.chop # removes last character
answer = gets.chomp.strip # removes spaces at the start
puts answer