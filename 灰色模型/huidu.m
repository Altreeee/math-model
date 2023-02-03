%灰度系统计算关联度的例题

%% 原书中例一代码-第一行是参考数列，下面都是比较数列，后两行需要调换顺序
clc,clear 
load x.txt %把原始数据存放在纯文本文件 x.txt 中
for i=1:15 
 x(i,:)=x(i,:)/x(i,1); %标准化数据
end 
for i=16:17 
 x(i,:)=x(i,1)./x(i,:); %标准化数据
end 
data=x; 
n=size(data,1); 
ck=data(1,:);m1=size(ck,1); 
bj=data(2:n,:);m2=size(bj,1); 
for i=1:m1 
 for j=1:m2 
 t(j,:)=bj(j,:)-ck(i,:); 
end 
 jc1=min(min(abs(t')));jc2=max(max(abs(t'))); 
 rho=0.5; 
 ksi=(jc1+rho*jc2)./(abs(t)+rho*jc2); 
 rt=sum(ksi')/size(ksi,2); 
 r(i,:)=rt; 
end 
r 
[rs,rind]=sort(r,'descend') %对关联度进行排序

%% 使用excel时，把数据复制到工作区，并将这个矩阵命名为X
% （1）在工作区右键，点击新建（Ctrl+N)，输入变量名称为X
% （2）在Excel中复制数据，再回到Excel中右键，点击粘贴Excel数据（Ctrl+Shift+V）
% （3）关掉这个窗口，点击X变量，右键另存为，保存为mat文件（下次就不用复制粘贴了，只需使用load命令即可加载数据）

%% 优势分析-多个y(参考)，多个x(比较)，x和y都竖着放，先放x再放y
%例二
clc,clear 
load data.txt %把原始数据存放在纯文本文件 data.txt 中
n=size(data,1); 
for i=1:n 
 data(i,:)=data(i,:)/data(i,1); %标准化数据
end 
ck=data(6:n,:);m1=size(ck,1); 
bj=data(1:5,:);m2=size(bj,1); 
for i=1:m1 
 for j=1:m2 
 t(j,:)=bj(j,:)-ck(i,:); 
 end 
 jc1=min(min(abs(t')));jc2=max(max(abs(t'))); 
 rho=0.5; 
 ksi=(jc1+rho*jc2)./(abs(t)+rho*jc2); 
 rt=sum(ksi')/size(ksi,2); 
 r(i,:)=rt; 
end 
r





