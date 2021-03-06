require "rubygems"
require "bunny"
require "json"

# Returns a connection instance
conn = Bunny.new ENV['CLOUDAMQP_URL']
# The connection is established when start is called
conn.start

# create a channel in the TCP connection
ch = conn.create_channel

# Declare a queue with a given name, examplequeue. In this example is a durable shared queue used.
q  = ch.queue("examplequeue", :durable => true)

# Bind a queue to an exchange
x = ch.direct("example.exchange", :durable => true)
q.bind(x, :routing_key => "process")

# Publish a message
information_message = "{\"email\": \"example@mail.com\",\"name\": \"name\",\"size\": \"size\"}"

x.publish(information_message,
  :timestamp      => Time.now.to_i,
  :routing_key    => "process"
)

sleep 1.0
conn.close