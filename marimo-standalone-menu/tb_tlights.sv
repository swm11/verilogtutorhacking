module tb_tlights();
   logic clk;
   logic rst_n;
   logic [2:0] rag;

   initial begin
      clk = 0;
      rst_n = 0;
      #20 rst_n = 1;
   end

   always #5 clk <= !clk;
   
   dut_tlights my_dut(.clk(clk), .rst_n(rst_n), .rag(rag));
   
   always @(negedge clk)
     begin
	$write("time=%04d: ctr=%3b=", $time,rag);
	if(rag[2]==1)
	  $write("<span style=\"background-color: red\"><b>R</b></span>");
	else
	  $write("<b>-</b>");
	if(rag[1]==1)
	  $write("<span style=\"background-color: orange\"><b>A</b></span>");
	else
	  $write("<b>-</b>");
	if(rag[0]==1)
	  $write("<span style=\"background-color: green\"><b>G</b></span>");
	else
	  $write("<b>-</b>");
	$display(" ");
	if($time>100)
	  $finish();
     end
   
endmodule // testbench_tlight

