%使用fluencer.xls计算每个人的追随者数
flu_name_T=flu_name';
tab=tabulate(flu_name_T);
[row,col]=size(tab);
j=1;
for i =1:row
    if tab(i,col)~=0
        tab_ful(j,:) = tab(i,:);
        j=j+1;
    end
end