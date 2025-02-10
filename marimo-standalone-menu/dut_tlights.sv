module dut_tlights(
                   input              clk,
                   input              rst_n,
                   output logic [2:0] rag);

   always_ff @(posedge clk or negedge rst_n)
     if(!rst_n)
       rag <= 3'b100;
     else
       begin
          case (rag)
            3'b100 : rag <= 3'b110;
            3'b110 : rag <= 3'b001;
            3'b001 : rag <= 3'b010;
            3'b010 : rag <= 3'b100;
            default : rag <= 3'b100;
          endcase
       end
endmodule // dut_tlights

