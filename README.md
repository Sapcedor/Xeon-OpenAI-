<h1>Xeon Chatbot</h1>

<p>This is a chatbot program built using the Tkinter library and the OpenAI API. The chatbot can be launched by running the python script <code>Xeon1.py</code>.</p>

<p>This chatbot is capable of holding a conversation with a user by generating responses to the user's messages using the OpenAI API. The chatbot is trained on a large dataset of text and is able to understand and respond to a wide range of topics and queries. The chatbot's responses can be customized by changing the `engine` parameter in the `chat` function, or by adjusting the `prompt` and `temperature` parameters to alter the chatbot's behavior. The chatbot's user interface is built using the Tkinter library, and can be customized using the various options available for Tkinter widgets.</p>


<h2>Dependencies</h2>

<ul>
  <li>tkinter</li>
  <li>openai</li>
</ul>

<p>If openai is not already installed, the script will automatically install it using <code>pip</code>.</p>

<h2>How to use</h2>

<ol>
  <li>Enter your OpenAI API key in the <code>openai.api_key</code> variable at the top of the script.</li>
  <li>Run the script using <code>python3 Xeon1.py</code></li>
  <li>Type a message in the input field at the bottom of the window and press enter to send it to the chatbot. The chatbot's response will be displayed in the chat window.</li>
  <li>To exit the program, type "exit" in the input field and press enter.</li>
</ol>

<h2>Customization</h2>

<p>The appearance and behavior of the chatbot can be modified by editing the code in the following sections:</p>

<h3>The <code>install_openai</code> function</h3>

<p>This function can be modified to install any other dependencies required by the script. Currently, this function only installs the <code>openai</code> package using <code>pip</code>, but you can add additional calls to <code>subprocess.run</code> to install any other packages that your script may require.</p>

<h3>The <code>chat</code> function</h3>

<p>This is where the chatbot's response is generated using the OpenAI API. You can modify the <code>engine</code> parameter to use a different OpenAI engine, or change the <code>prompt</code> and <code>temperature</code> parameters to alter the chatbot's behavior. For example, you could change the <code>temperature</code> parameter from <code>0</code> to a higher value to make the chatbot's responses more creative and unpredictable.</p>

<h3>The <code>handle_user_input</code> function</h3>

<p>This function is called whenever the user submits an input. You can modify this function to add additional functionality, such as saving the conversation to a file or performing additional processing on the user's input. For example, you could add code to store the user's input in a database, or to send an email or text message when certain keywords are detected in the user's input.</p>

<h3>The Tkinter widgets</h3>
<p>(e.g. <code>root</code>, <code>display_frame</code>, <code>user_input_entry</code>) can be customized using their various options (e.g. <code>bg</code>, <code>fg</code>, <code>font</code>). Consult the Tkinter documentation for a full list of options. You can use these options to change the appearance and layout of the chatbot's user interface. For example, you could change the background color of the main window using the <code>root.configure(bg='color')</code> function, or change the font of the user input field using the <code>font</code> option of the <code>user_input_entry</code> widget.</p>

<h2>License</h2>

<p>This project is licensed under an open source license. An open source license allows you to use, modify, and distribute the software freely as long as you acknowledge the original authors and distribute your modifications under the same license. For more information, see the <a href="https://opensource.org/licenses">Open Source Initiative</a> website.</p>

<h2>Acknowledgments</h2>

<ul>
  <li>The Tkinter library documentation was used as a reference for building the user interface.</li>
  <li>The OpenAI API was used to generate the chatbot's responses.</li>
</ul>
