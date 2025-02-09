module dut(
	   input	      clk,
	   input	      rst_n,
	   output logic [7:0] ctr);

   always_ff @(posedge clk or negedge rst_n)
     if(!rst_n)
       ctr <= 0;
     else
       ctr <= ctr+3;
endmodule // dut
