
    <!-- Modal for edit -->
  <div class="modal fade" id="editModal" tabindex="-1" role="dialog" aria-labelledby="editModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="editModalLabel">写日记</h4>
        </div>
        <div class="modal-body">
          <form action="/imm/index" method="POST">
          <div class="form-group" >
          <input name="username" type="text" id="username"/>

           <div class="form-group" >
         <label for="emotionType" class=" control-label">情绪类型</label>
            <div class="dropdown">
                <select class="form-control" id="emotionType" name="emotionType">
                    <option>Fear</option>
                    <option>Depression</option>
                    <option>Anger</option>
                    <option>Disgust</option>
                    <option>Joy</option>
                </select>
            </div>
        </div>  
           <div class="form-group" >
         <label for="flowValue" class=" control-label">心流值</label>
            <div class="dropdown">
                <select class="form-control" id="flowValue" name="flowValue">
                    <option>0</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>                    
                    <option>6</option>
                    <option>7</option>
                    <option>8</option>
                    <option>9</option>
                </select>
            </div>
        </div>  
                <div class="form-group" >
           <label for="tireness" class=" control-label">疲劳度</label>
            <div class="dropdown">
                <select class="form-control" id="tireness" name="tireness">
                    <option>0</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>                    
                    <option>6</option>
                    <option>7</option>
                    <option>8</option>
                    <option>9</option>
                </select>
            </div>
        </div> 
        <div class="form-group" >
        <label for="tpFeeling" class="control-label">温度感觉</label>
          <div class="dropdown">
                <select class="form-control" id="tpFeeling" name="tpFeeling">
                    <option>0</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>
            </div>   
        <div class="form-group">
           <label for="diaryContent" class="control-label">你的感受和想法</label>

              <textarea class ="form-control" name="diaryContent"
              id="diaryContent"
              placeholder="Leave a comment"
              aria-label="Comment body"
              ></textarea>

            <button class="btn btn-primary" type="submit" id="submitData">提交</button>
          </form>
        </div>
      </div>
    </div>
  </div> 



</body>

</html>
