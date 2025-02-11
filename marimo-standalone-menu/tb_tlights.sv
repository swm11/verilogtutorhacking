module tb_tlights();
   logic clk;
   logic rst_n;
   logic [2:0] rag;

   // add readable trace signals
   logic       red, amber, green;
   always_comb begin
      red = rag[2];
      amber = rag[1];
      green = rag[0];
   end
   
   initial begin
      // dump traces so we can see waveforms of signals
      $dumpfile("obj_dir/tb_tlights_trace.vcd");
      $dumpvars(clk, rst_n, red, amber, green);
      // initialise clock and reset
      clk = 1;
      rst_n = 0;
      #15 rst_n = 1;
   end

   always #5 clk <= !clk;
   
   dut_tlights my_dut(.clk(clk), .rst_n(rst_n), .rag(rag));
   
   always @(negedge clk)
     begin
	$write("time=%04d: ctr=%3b=", $time,rag);
	if(red)
	  $write("<span style=\"background-color: red\"><b>R</b></span>");
	else
	  $write("<b>-</b>");
	if(amber)
	  $write("<span style=\"background-color: orange\"><b>A</b></span>");
	else
	  $write("<b>-</b>");
	if(green)
	  $write("<span style=\"background-color: green\"><b>G</b></span>");
	else
	  $write("<b>-</b>");
	$display(" ");
	if($time>130)
	  $finish();
     end

endmodule // testbench_tlight

