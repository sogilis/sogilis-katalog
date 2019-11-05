with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Text_IO;         use Ada.Text_IO;

procedure Roman_2_Decimal is
   Input_Length : Natural := 100;
   Input_String : String (1 .. Input_Length);
begin
   Get_Line (Input_String, Input_Length);

   if Input_Length > 0 then
      Put (Input_Length, Width => 1);
   end if;
end Roman_2_Decimal;
