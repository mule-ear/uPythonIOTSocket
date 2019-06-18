require 'socket'        # Sockets are in standard library

hostname = '192.168.22.106'
port = 5020

s = TCPSocket.open(hostname, port)
puts s

run = true
while run do
  puts "Message: "
  inp = gets.chomp
  s.write( inp )
  reply = s.recv(100)
  puts "Reply == " + reply.chomp
  if inp == "QUIT" 
    run = false
  end
end
puts "Closing connection."
s.close
