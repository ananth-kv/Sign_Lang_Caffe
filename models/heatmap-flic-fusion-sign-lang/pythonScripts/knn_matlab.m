function knn_matlab(Xtest)

[vectorFileList, labelFileList] = textread('/hdd2/datasets/ASL/knnFile.txt','%s %s');
Xtrain = [];
for i=1:length(vectorFileList)
    %% Get the vector from each .out file
    path = vectorFileList(i);
    vector = textread(path{1}, '%f');
    vector = transpose(vector);
    Xtrain = [Xtrain; vector];
    
end

testVector = textread(Xtest, '%f');
testVector = transpose(testVector);

DistMatrix = dist2(Xtrain,testVector);
[closePairs, Idx] = sort(DistMatrix);

%% Top K-points or top-point
TopIdx = Idx(1:3,:);

for k = 1:size(TopIdx,1)
    path = labelFileList(TopIdx(k,1));
    y_hat = textread(path{1}, '%s').';
    display(y_hat);
end

end
