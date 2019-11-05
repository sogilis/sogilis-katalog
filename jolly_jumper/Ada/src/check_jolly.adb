with Ada.Text_IO; use Ada.Text_IO;

procedure Check_Jolly is
   Input_Length : Natural := 100;
   Input_String : String (1 .. Input_Length);
begin
   Get_Line (Input_String, Input_Length);
   Put ("OK");
end Check_Jolly;
