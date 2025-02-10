module tb_counter();
   logic clk;
   logic rst_n;
   logic [7:0] result;

   initial begin
      clk = 0;
      rst_n = 0;
      #20 rst_n = 1;
   end

   always #5 clk <= !clk;
   
   dut_counter my_dut(.clk(clk), .rst_n(rst_n), .ctr(result));
   
   always @(negedge clk)
     begin
	$display("time=%04d: ctr=%d", $time, result);
	if($time>100)
	  $finish();
     end
   
endmodule // testbench
