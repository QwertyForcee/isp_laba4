import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dynhead',
  templateUrl: './dynhead.component.html',
  styleUrls: ['./dynhead.component.css']
})
export class DynheadComponent implements OnInit {

  constructor() { }

  dynhead:DynamicService=new DynamicService();
  ngOnInit(): void {
    this.dynhead.Cicle()
  }


}
class DynamicService{
  CurrentExpr:string="return x";
  CurrentString:string="";
  index:number=0;
  expretions:string[]=[
    "return x**y",
    "return x-y",
    "return x[:y]",
    "return x"
  ]
  async Cicle(){
    await this.Write();
    await this.delay(1000);
    await this.Backspace();
    this.Cicle();
  }
  //задержка.
  readonly MsCount:number=100;

   async Write():Promise<boolean>{
    for(let i=0;i<this.CurrentExpr.length;i++){
      this.CurrentString+=this.CurrentExpr[i];
      await this.delay(this.MsCount);
    }
    if(this.index==this.expretions.length-1)
    {
      this.index=0;

    }
    else
    {
       ++this.index;
    }
    this.CurrentExpr=this.expretions[this.index];
    return true;
  }
  async Backspace():Promise<boolean>{
    let lnth:number=this.CurrentString.length;
    for(let i=0;i<lnth;i++){
      this.CurrentString=this.CurrentString.slice(0,-1);
      await this.delay(this.MsCount);
    }
    return true;
  }
  private delay(ms:number){
    return new Promise(resolve=>setTimeout(resolve,ms));
  }

}

