function knn_matlab(Xtest)

[vectorFileList, labelFileList] = textread('/hdd2/datasets/ASL/knnFile.txt','%s %s');
% Xtrain = zeros(length(vectorFileList),2400);
% for i=1:length(vectorFileList)
%     %% Get the vector from each .out file
%     path = vectorFileList(i);
%     vector = textread(path{1}, '%f');
%     vector = transpose(vector);
%     Xtrain(i,:) = vector;
%     
% end
% save('Xtrain.mat','Xtrain');
load('Xtrain.mat','Xtrain');
testVector = textread(Xtest, '%f');
testVector = transpose(testVector);

DistMatrix = dist2(Xtrain,testVector);
[closePairs, Idx] = sort(DistMatrix);

%% Top K-points or top-point
TopIdx = Idx(1:3,:);
labels = zeros(size());
for k = 1:length(labelFileList,1)
    path = labelFileList(k,1);
    y_hat = textread(path{1}, '%s').';
    %display(y_hat);
    
end

end
