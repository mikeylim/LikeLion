def ask_person
    puts "누가 참여하는지 알려주세요! >> "
    personList = gets.chomp.split(" ") # ['1st element', '2nd element', '3rd element']

    puts "며칠간 설문을 할 지 알려주세요! >> "
    numOfDays = gets.chomp.to_i # converts string into Int
    # initializing array into global variable @meeting which is hash
    @meeting = {}
    1.upto(numOfDays) do |day|
        @meeting[day] = []
    end
    # for each person
    personList.each do |person|
        # for everyday from 1 to numOfDays
        1.upto(numOfDays) do |day|
            puts "#{person} (은/는) [#{day}]날에 시간이 되면 Y/y를 누르세요. >> " 
            
            answer = gets.chomp
            if (answer.downcase == 'y') # regardless of capital
                @meeting[day] << person # store that person (value) into the current day (key)
            end
        end
    end
end

def print_meeting
    @meeting.each do |day,person|
        puts day.to_s + "일에 시간되는 사람(들) - " + person.to_s
    end
end

ask_person
print_meeting